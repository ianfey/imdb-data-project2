Dimensional Modeling Description
The IMDb data warehouse is structured using a star schema to support efficient analytical queries. This model separates quantitative metrics (stored in the fact table) from descriptive information (stored in dimension tables), allowing for scalable, flexible analysis.

At the center is the fact_movies table, which captures measurable data such as the number of user votes and average ratings for each movie. Each entry in the fact table is uniquely identified by a surrogate key and references several dimension tables through foreign keys.

Fact Table: fact_movies
fact_id (surrogate primary key)

title_id → links to dim_titles

rating_id → links to dim_ratings

crew_id → links to dim_crew

numVotes, averageRating

This table holds the core metrics used in analysis, such as total user votes and the average rating per movie.

Dimension Tables
dim_titles: Contains movie title, genre, year, and runtime

dim_ratings: Stores rating and vote count data

dim_crew: Maps each movie to its director(s) and writer(s)

dim_people: Includes biographical details such as name, birth year, and profession

This model enables analysis across multiple perspectives, including:

Top-rated movies by genre and decade

Comparison of average ratings between directors

Tracking a specific director or writer’s contributions over time

The use of surrogate keys ensures consistency and simplifies joins between tables. The star schema provides the flexibility to answer a variety of business questions quickly and accurately.
