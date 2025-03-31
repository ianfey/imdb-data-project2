## IMDb Data Warehouse Project
This project utilizes the IMDb dataset. The purpose of the project is to analyze and model film metadata, using a star schema, for the purpose of querying and deriving insights.
Data Source
## IMDb Datasets: https://www.imdb.com/interfaces/
## Files Used: title.basics.tsv, title.ratings.tsv, title.crew.tsv, name.basics.tsv
## Data Dictionary 
Available Here: https://www.imdb.com/interfaces/
## Project Overview
This project draws on the IMDb dataset. The main goal was to design a data warehouse for easy querying and analysis of worldwide movie data, such as trends in genres, ratings, and crew activity.
The .tsv files provided by IMDb were used as raw data sources will be cleaned using an ETL process, and structured into a star schema. The star schema references a central fact table with key information such as average ratings and votes, along with several dimension tables containing movie metadata, crew information, and biographic data.

