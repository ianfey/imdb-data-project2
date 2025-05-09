IMDb Data Warehouse – CIS4400 Project
Overview
We built a dimensional data warehouse for IMDb film metadata. We designed it for fast queries. We designed it for analytical flexibility. We designed it for clear insights into movies, people, genres, and ratings.

##Source Data##
We used four public IMDb .tsv.gz files:

title.basics.tsv.gz – provides title, type, year, and genres

title.ratings.tsv.gz – provides average rating and number of votes

title.crew.tsv.gz – provides directors and writers

name.basics.tsv.gz – provides birth year, professions, and primary names

These files came from https://datasets.imdbws.com. These files followed a tab-separated format. These files updated daily.

ETL Pipeline
We extracted the data using Python. We transformed the data with pandas. We loaded the cleaned data into Redshift.

We split columns that had multiple values for each field seperated by commas, removed nulls, and standardized types. The date was already in YYY-MM-DD format and had the column start year which could be used as the filter for analysis.
We dropped unneeded columns. We selected only relevant entries. We ensured consistent primary keys.

We stored intermediate files in Azure Blob Storage.

Blob Storage Details
We used container raw-imdb for raw files. We used cleaned-imdb for transformed outputs. We used consistent date-stamped prefixes to track uploads.

Data Model
We followed a star schema.

Fact Table: fact_ratings – holds tconst, rating, and vote counts

Dimension Tables:

dim_title – describes title, year, genres

dim_people – captures first name, last name, and birth year

dim_crew – lists directors and writers

dim_genre – breaks out individual genres

Each dimension uses a surrogate key. Each fact references these dimensions through foreign keys. Each table uses appropriate encoding and compression.


Redshift Deployment
We created a serverless Redshift workgroup. We used IAM roles to load from S3. We connected via Query Editor v2.

We first created the tables and then loaded cleaned CSVs into the created tables.

We verified row counts and schemas.

We performed joins to validate keys and created a final analytics table which would be used to perform analysis on in Quicksight.

Final Dashboard
We connected Redshift to Quicksight. We visualized average ratings by genre, volume over time and by genre, and top writers professions by rating.

Charts were clean. Charts were labeled. Charts were interactive.

Filters included year, genre, and title type.

Project Objectives
We aimed to build a complete pipeline. We aimed to apply ETL principles. We aimed to create actionable insights for film analytics.
