+---------------------+
|   Source Systems    |
+---------------------+
| IMDb.com datasets   |
| Structured .tsv.gz  |
| - title.basics.tsv.gz |
| - title.ratings.tsv.gz |
| - title.crew.tsv.gz   |
| - name.basics.tsv.gz  |
+---------------------+
          |
          v
+--------------------------+
|     Ingestion Layer      |
+--------------------------+
| Language: Python 3.11    |
| Libraries:               |
| - requests               |
| - os                     |
| - pandas                 |
|                          |
| Cloud: Azure Blob Storage|
| - Raw Files Container    |
| - Cleaned CSV Container  |
+--------------------------+
          |
          v
+--------------------------+
|     Processing Layer     |
+--------------------------+
| ETL Pipeline Steps:      |
| - Remove nulls/malformed |
| - Normalize fields       |
| - Convert dates to YYYY-MM-DD |
| - Join related datasets  |
+--------------------------+
          |
          v
+--------------------------+
|     Data Warehouse       |
+--------------------------+
| Platform: Amazon Redshift|
| Tables:                  |
| - fact_ratings           |
| - dim_title              |
| - dim_people             |
| - dim_crew               |
+--------------------------+
          |
          v
+--------------------------+
|   Presentation Layer     |
+--------------------------+
| Tool: AWS QuickSight     |
| Visuals:                 |
| - Ratings by Genre       |
| - Trends over Time       |
| - Heatmaps of Activity   |
+--------------------------+
