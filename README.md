
# IMDb Data Warehouse Project

This project is based on the IMDb dataset, designed for CIS4400 Homework 1. The goal is to analyze and model film metadata using a star schema for efficient querying and insight generation.

## Data Source
- IMDb Datasets: https://www.imdb.com/interfaces/
- Files used: `title.basics.tsv`, `title.ratings.tsv`, `title.crew.tsv`, `name.basics.tsv`


## Data Dictionary
Refer to: https://www.imdb.com/interfaces/


## Project Summary
This project is built around the publicly available IMDb dataset. The main objective was to design a data warehouse that enables efficient querying and analysis of global movie data, including trends in genres, ratings, and crew activity.

Using the raw .tsv files provided by IMDb, the data was cleaned and transformed through an ETL process, then structured into a star schema. The schema includes one central fact table containing key metrics (e.g., average ratings, vote counts) and multiple dimension tables capturing movie metadata, crew details, and biographical information.

The project also includes:

A GitHub repository for version control and collaboration

A documented data model with a full explanation and visual diagram

Architecture diagrams showing the flow of data and system interactions

A clear breakdown of business and functional requirements

This foundation will support future homework assignments involving more advanced analytics and data visualization, using the same IMDb dataset as the core data source.

