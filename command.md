python -m venv venv
venv\Scripts\Activate.ps1
deactivate


pip install python-dotenv




docker compose up -d // -d runs in the background
docker compose down




 docker ps

docker volume ls


docker compose up -d --build //allows rebuilding wihtout lossing the previous things.

// this make sure the file is executable
chmod +x ./docker/postgres/init-multiple-databases.sh
docker compose down -v
docker compose up --build

docker compose up -d --force-recreate


# airflow

docker exec -it airflow-scheduler bash
env | grep AIRFLOW_VAR
airflow varialbes list

docker exec -it airflows-worker bash


cd /opt/airflow/logs
find . | grep get_playlist_id

cat './dag_id=produce_json/run_id=manual__2026-05-28T21:54:35.165424+00:00/task_id=get_playlist_id/attempt=1.log'


## SQL

docker exec -it postgres psql -U yt_api_user -d elt_db

\du
\l

### Getting schema
 \dt core.*



 # testing

 we build a second version.

docker build -t sl/yt_api_elt:1.0.1 .

## running soda

https://docs.soda.io/soda-documentation/soda-v3/data-source-reference/connect-postgres
soda test-connection -d pg_datasource -c /opt/airflow/include/soda/configuration.yml -V


running the checks

soda scan -d pg_datasource -c /opt/airflow/include/soda/configuration.yml -v SCHEMA-core /opt/airflow/include/soda/checks.yml