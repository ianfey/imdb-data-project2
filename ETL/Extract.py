import os
from azure.storage.blob import BlobServiceClient
from datetime import date

# CONFIGURATION 
CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=imdbwarehouse;AccountKey=FeT/mWcISIWwyAgGKpoQEEGsloqMJbzlOQX8ZZeIQndAFVAVOPJQd5A1655EswxJ/B5tgoewaMN1+ASt0hLcsQ==;EndpointSuffix=core.windows.net"
CONTAINER_NAME = "raw-imdb"  
LOCAL_FOLDER = "/Users/ianfeygels/Downloads"  
BLOB_PREFIX = f"{date.today().isoformat()}/raw/"  

# CONNECT TO BLOB STORAGE 
blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)
container_client = blob_service_client.get_container_client(CONTAINER_NAME)

#  UPLOAD FILES 
for filename in os.listdir(LOCAL_FOLDER):
    if filename.endswith(".tsv.gz"):
        file_path = os.path.join(LOCAL_FOLDER, filename)
        blob_name = BLOB_PREFIX + filename

        print(f"Uploading {filename} to {blob_name}...")

        with open(file_path, "rb") as data:
            container_client.upload_blob(name=blob_name, data=data, overwrite=True)

print(" All IMDb files uploaded successfully.")
