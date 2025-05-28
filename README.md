# Movie Data Pipeline (2010–2020)

This project demonstrates a full ELT pipeline using Spark and Databricks.

## Goals:
- Extract movie data from TMDB (or local CSV)
- Build a Lakehouse architecture with Bronze → Silver → Gold
- Analyze genre popularity, average ratings by year

## Tech Stack:
- Python, PySpark, Databricks
- Spark SQL
- Power BI (for visualization)

## Structure:
- **Bronze**: raw data ingestion
- **Silver**: cleaning (nulls, formatting, filtering)
- **Gold**: aggregation by genre/year/popularity

## Insights:
- Dramatic increase in Action and Sci-Fi movies post-2015
- Documentaries have highest average rating
- Popularity of Horror peaks around Halloween

## Setup:
1. Clone repo
2. Upload CSV to DBFS
3. Run notebooks in order
