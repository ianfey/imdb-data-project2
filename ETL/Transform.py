import pandas as pd
from azure.storage.blob import BlobServiceClient
import os
from datetime import datetime
from io import StringIO
import time

print("Starting optimized IMDb data transformation script...")

# Azure config
connection_string = "DefaultEndpointsProtocol=https;AccountName=imdbwarehouse;AccountKey=FeT/mWcISIWwyAgGKpoQEEGsloqMJbzlOQX8ZZeIQndAFVAVOPJQd5A1655EswxJ/B5tgoewaMN1+ASt0hLcsQ==;EndpointSuffix=core.windows.net"
container_name = "transfromed-imdb"
local_path = "/Users/ianfeygels/Downloads"
timestamp = datetime.now().strftime("%Y%m%d")
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

def upload_df_to_blob(df, name_prefix):
    output_filename = f"{name_prefix}_{timestamp}.csv"
    blob_path = f"cleaned/{output_filename}"
    print(f"Uploading to Azure Blob: {blob_path}...")

    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=False)
    csv_buffer.seek(0)

    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_path)
    blob_client.upload_blob(csv_buffer.getvalue(), overwrite=True)
    print(f"Upload complete: {blob_path}")

def filter_tsv_by_column(filepath, col, valid_ids):
    chunks = pd.read_csv(filepath, sep='\t', dtype=str, chunksize=500_000)
    return pd.concat(chunk[chunk[col].isin(valid_ids)] for chunk in chunks)

# 1. Load ratings first and extract valid tconsts
print("Processing title.ratings.tsv.gz...")
ratings = pd.read_csv(os.path.join(local_path, "title.ratings.tsv.gz"), sep="\t", dtype=str)
valid_tconsts = set(ratings['tconst'])
upload_df_to_blob(ratings, "cleaned_title_ratings")
print("\u2713 Completed ratings\n")

# 2. Process title.basics.tsv.gz (filtered by valid tconsts)
print("Processing title.basics.tsv.gz...")
title_basics = filter_tsv_by_column(os.path.join(local_path, "title.basics.tsv.gz"), 'tconst', valid_tconsts)
genres_split = title_basics['genres'].str.split(",", expand=True)
genres_split.columns = [f"genre_{i+1}" for i in range(genres_split.shape[1])]
title_basics = pd.concat([title_basics.drop(columns=['genres']), genres_split], axis=1)
upload_df_to_blob(title_basics, "cleaned_title_basics")
print("\u2713 Completed basics\n")

# 3. Process title.crew.tsv.gz (fully optimized block)
print("Processing title.crew.tsv.gz...")
start = time.time()

try:
    del title_basics, genres_split
except:
    pass

try:
    title_crew = filter_tsv_by_column(os.path.join(local_path, "title.crew.tsv.gz"), 'tconst', valid_tconsts)

    title_crew['directors'] = title_crew['directors'].replace('\\N', '').str.split(',').str[0]
    title_crew['writers'] = title_crew['writers'].replace('\\N', '').str.split(',').str[0]

    title_crew_cleaned = title_crew[['tconst', 'directors', 'writers']]

    upload_df_to_blob(title_crew_cleaned, "cleaned_title_crew")
    print(f"\u2713 Completed crew in {round(time.time() - start, 2)} seconds\n")

except Exception as e:
    print("Error processing title.crew.tsv.gz:", e)

# 4. Process name.basics.tsv.gz (filtered by nconsts in crew)
print("Processing name.basics.tsv.gz...")
crew_ids = pd.concat([title_crew_cleaned['directors'], title_crew_cleaned['writers']]).dropna().unique()
valid_nconsts = set(crew_ids)
name_basics = filter_tsv_by_column(os.path.join(local_path, "name.basics.tsv.gz"), 'nconst', valid_nconsts)

name_basics[['firstName', 'lastName']] = name_basics['primaryName'].str.extract(r'^(\S+)\s+(.*)$')
prof_cols = name_basics['primaryProfession'].str.split(",", expand=True)
prof_cols.columns = [f"profession_{i+1}" for i in range(prof_cols.shape[1])]
known_cols = name_basics['knownForTitles'].str.split(",", expand=True)
known_cols.columns = [f"knownFor_{i+1}" for i in range(known_cols.shape[1])]

name_basics = pd.concat([name_basics.drop(columns=['primaryName', 'primaryProfession', 'knownForTitles']), prof_cols, known_cols], axis=1)

upload_df_to_blob(name_basics, "cleaned_name_basics")
print("\u2713 Completed name.basics\n")

print("\u2705 All files processed and uploaded successfully.")
