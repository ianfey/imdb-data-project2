The IMDb data warehouse is structured using a star schema. The model separates facts from context. The model separates measures from descriptions. The model creates clarity, consistency, and speed.

At its center is the fact_movies table. It stores key metrics such as vote counts and rating averages. It identifies each record with a surrogate key. It connects to dimension tables through foreign keys.

Fact Table: fact_movies

fact_id: surrogate primary key

title_id: joins to dim_titles

rating_id: joins to dim_ratings

crew_id: joins to dim_crew

numVotes, averageRating: core performance indicators

Dimension Tables

dim_titles: provides the title, the genre, the year, and the runtime

dim_ratings: includes the rating value and total votes

dim_crew: links each film to its director and writer

dim_people: lists name, birth year, and profession

The schema enables multiple perspectives. The schema enables comparisons across time. The schema enables insight into individuals and groups.

You can identify top-rated films by genre. You can compare directors across decades. You can trace a writer’s career over time. You can observe changes in audience feedback.

Surrogate keys ensure referential consistency. Foreign keys reduce redundancy. The design improves query speed. The structure improves analytical flexibility.

This model is built for scale. This model is built for insight. This model is built for action.
