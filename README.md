# YT_ELT


docker build -t sl/yt_api_elt:1.0.0 .


docker compose down -v
docker compose up --build


Glossary:

ETL - extract, transform, load
DAG - Directed Cyclic Graph

Soda helps you check whether your data is:

Complete
Accurate
Consistent
Fresh