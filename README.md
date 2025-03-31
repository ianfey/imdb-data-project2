IMDb Data Warehouse Project
This project utilizes the IMDb dataset provided in CIS4400 Homework 1. The purpose of the project is to analyze and model film metadata, using a star schema, for the purpose of querying and deriving insights.

Data Source
IMDb Datasets: https://www.imdb.com/interfaces/

Files Used: title.basics.tsv, title.ratings.tsv, title.crew.tsv, name.basics.tsv

Data Dictionary
Available Here: https://www.imdb.com/interfaces/

Project Overview
This project draws on the publicly available IMDb dataset. The main goal was to design a data warehouse for easy querying and analysis of worldwide movie data, such as trends in genres, ratings, and crew activity.

The .tsv files provided by IMDb were used as raw data sources and cleaned using an ETL process, and structured into a star schema. The star schema referenced a central fact table with key information such as average ratings and votes, along with several dimension tables containing movie metadata, crew information, and biographic data.

The Project Also Contains:
A GitHub repository for version control and collaborative development

Documented data model with explanation and diagram

Architectural diagram indicating data flow and system participation

Clear breakdown of business and functional requirements

This framework serves as a basis for future homework assignments engaging in more complicated analysis and visualizations of data, using the IMDb dataset as the source of data.

