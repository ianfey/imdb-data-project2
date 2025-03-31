The data architecture defines how the raw IMDb datasets are collected, cleaned, structured, and stored to support efficient querying and analysis. Data is sourced from IMDb’s TSV files, including title.basics.tsv, title.ratings.tsv, title.crew.tsv, and name.basics.tsv.

An ETL pipeline will be used to clean missing values, normalize columns (such as genres or dates), and integrate related records via primary keys (e.g., tconst for titles, nconst for people). Once cleaned, the data will be loaded into a relational database following a star schema format, with a central fact table capturing metrics like ratings and votes, and dimension tables for titles, people, genres, and crew.

This architecture supports scalability, consistency, and fast query performance—ideal for large-scale analysis of entertainment trends.
