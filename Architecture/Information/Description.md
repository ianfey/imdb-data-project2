IMDb Data Architecture – CIS4400 Project
Source Systems
IMDb offers data. IMDb serves structure. IMDb updates daily.

The dataset arrives in .tsv.gz format. It uses tabs for separation. It uses UTF-8 for encoding.

Included files:

title.basics.tsv.gz: film types, release years, genres

title.ratings.tsv.gz: average ratings, vote counts

title.crew.tsv.gz: director links, writer links

name.basics.tsv.gz: person names, professional roles

Each file is retrieved by script. Each file is stored on Azure. Each file includes a timestamp.

Ingestion Layer
Language: Python 3.11
Libraries Used:

requests, os – to fetch and to organize

pandas – to load and to clean

azure-storage-blob – to send and to archive

The pipeline retrieves the files. The pipeline decompresses the archives. The pipeline uploads the results.

Raw and cleaned files are saved. Raw and cleaned versions are dated. Raw and cleaned records are preserved.

Storage Layer
Platform: Azure
Service: Blob Storage – Hot Tier

Two containers are created. One stores raw data. One stores transformed outputs.

File Naming Structure:

Raw: 2025-05-06/raw/title.basics.tsv.gz

Cleaned: 2025-05-06/transformed/title.basics_cleaned.csv

There are no duplicates. There are no naming errors. There are no missed files.

Processing Layer
Pipeline Type: ETL — extract, transform, load

We remove missing records. We reformat all dates. We compute derived fields.
We split compound values. We join foreign references. We align each schema.

Every step is recorded. Every step is validated. Every step is repeatable.

Redshift stores final outputs. Redshift organizes them by table. Redshift readies them for analysis.

Semantic Layer
Grain: one row per title per rating

Fact Table: fact_ratings

Primary Key: fact_id

Foreign Key: tconst

Metrics:

average_rating

num_votes

Dimension Tables:

dim_title — genres, durations, release years

dim_people — individuals in cast or crew

dim_crew — mappings to directors and writers

Each table is linked. Each key is synthetic. Each row is traceable.

Presentation Layer
Tool: AWS QuickSight

The dashboards show trends. The dashboards expose gaps. The dashboards surface patterns.

You view ratings by category. You view changes by decade. You view peaks by country.
You analyze director popularity. You analyze genre distribution. You analyze audience engagement.

QuickSight connects directly. QuickSight queries Redshift. QuickSight drives insight.

