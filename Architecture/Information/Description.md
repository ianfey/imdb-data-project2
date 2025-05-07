# IMDb Data Architecture – CIS4400 Project

## Source Systems
IMDb offers. IMDb serves. IMDb updates.

The dataset comes in `.tsv.gz` format. It uses tabs. It uses UTF-8 encoding. It updates daily.

Included files:
- `title.basics.tsv.gz`: types, years, genres
- `title.ratings.tsv.gz`: averages, votes
- `title.crew.tsv.gz`: directors, writers
- `name.basics.tsv.gz`: names, roles

Each file is downloaded by script. Each file is stored on Azure. Each file is timestamped.

## Ingestion Layer
**Language**: Python 3.11  
**Libraries Used**:
- `requests`, `os` – for fetching and file paths
- `pandas` – for loading and transforming
- `azure-storage-blob` – for pushing to cloud

The process retrieves. The process unpacks. The process uploads.

Raw and cleaned versions are saved. Versions are sorted by date. Versions are preserved for audit.

## Storage Layer
**Platform**: Azure  
**Service**: Blob Storage (Hot Tier)

There are two containers. One holds raw files. One holds cleaned CSVs.

**Filenames** follow a structure:
- Raw: `2025-05-06/raw/title.basics.tsv.gz`
- Cleaned: `2025-05-06/transformed/title.basics_cleaned.csv`

No conflicts. No ambiguity. No gaps.

## Processing Layer
**Pipeline Type**: ETL – extract, transform, load

We drop incomplete rows. We reformat all dates. We add calculated fields.  
We split multi-value entries. We join across foreign keys.

Every transformation is logged. Every step is validated. Every file is schema-aligned.

Redshift stores the final outputs. Redshift stores them by table. Redshift stores them for analytics.

## Semantic Layer
**Grain**: one row per title per rating

**Fact Table**: `fact_ratings`  
- Primary key: `fact_id`  
- Foreign key: `tconst`  
- Measures:
  - `average_rating`
  - `num_votes`

**Dimensions**:
- `dim_title` — genres, runtime, release year
- `dim_people` — individuals from cast or crew
- `dim_crew` — links to directors, links to writers

Each key is synthetic. Each table is related. Each row is traceable.

## Presentation Layer
**Tool**: AWS QuickSight

The dashboards compare. The dashboards visualize. The dashboards respond.

You see ratings by genre. You see trends by decade. You see spikes by country.  
You explore popular directors. You explore genre frequency. You explore vote volume.

QuickSight connects live. QuickSight reads from Redshift. QuickSight powers decisions.
