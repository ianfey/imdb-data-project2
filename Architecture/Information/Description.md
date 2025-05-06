from pathlib import Path

# Markdown content
md_content = """
# 🎬 IMDb Data Architecture – CIS4400 Project

## 📥 Source Systems
**IMDb.com** provides structured `.tsv.gz` files through its public dataset interface at [https://datasets.imdbws.com](https://datasets.imdbws.com). Files include movie metadata (e.g., titles, ratings, people, and crew). All files follow a tab-separated format with UTF-8 encoding and are updated daily.

Key source files:
- `title.basics.tsv.gz`: title type, year, genres
- `title.ratings.tsv.gz`: average rating, number of votes
- `title.crew.tsv.gz`: directors, writers
- `name.basics.tsv.gz`: actor/crew metadata

All files are downloaded programmatically using Python and stored in Azure Blob Storage.

## 🧪 Ingestion Layer
**Language**: Python 3.11  
**Libraries**:
- `requests` and `os` – for downloading raw IMDb files
- `pandas` – for parsing `.tsv` and transforming
- `azure-storage-blob` – to upload raw and cleaned files to Azure Blob Storage

The pipeline downloads the latest IMDb `.tsv.gz` files, decompresses and parses them, and uploads both raw and transformed versions to Azure Blob. Files are timestamped by processing date to ensure version control.

## 🗄 Storage Layer
**Platform**: Microsoft Azure  
**Service**: Azure Blob Storage (Hot Tier)

Containers:
- `raw-imdb`: unmodified `.tsv.gz` IMDb files
- `transformed-imdb`: cleaned `.csv` files ready for warehousing

**File naming conventions**:
- Raw: `2025-05-06/raw/title.basics.tsv.gz`
- Cleaned: `2025-05-06/transformed/title.basics_cleaned.csv`

## ⚙️ Processing Layer
**Strategy**: ETL pipeline (Extract → Transform → Load)

Transformations include:
- Removing null or malformed values
- Converting date fields to `YYYY-MM-DD` format
- Creating derived fields such as `decade`, `isAdult (bool)`
- Normalizing multi-value fields (`genres`, `professions`)
- Joining and mapping keys across related datasets (`tconst`, `nconst`)

All data is verified against IMDb’s schema. ETL outputs are loaded into Redshift.

## 🧠 Semantic Layer
**Grain**: One row per rating per title

**Fact Table**: `fact_ratings`
- PK: `fact_id`
- FK: `tconst`
- Measures:
  - `average_rating`
  - `num_votes`

**Dimension Tables**:
- `dim_title` — title metadata (e.g., genre, runtime, year)
- `dim_people` — actor/crew metadata
- `dim_crew` — directors and writers associated with each title

**Keys**: surrogate PKs, `tconst`, `nconst`

## 📊 Presentation Layer
**Tool**: AWS QuickSight

Dashboards provide:
- Rating distribution across genres, decades, and countries
- Line charts showing rating trends over time
- Heatmaps of most active directors/writers
- Pie charts of genre frequency

QuickSight connects directly to Redshift and uses date filtering controls for dynamic visuals.
"""

