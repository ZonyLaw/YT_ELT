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


# airflow

docker exec -it airflow-scheduler bash
env | grep AIRFLOW_VAR
airflow varialbes list


cd /opt/airflow/logs
find . | grep get_playlist_id

cat './dag_id=produce_json/run_id=manual__2026-05-28T21:54:35.165424+00:00/task_id=get_playlist_id/attempt=1.log'


## SQL

docker exec -it postgres psql -U yt_api_user -d elt_db

\du
\l

### Getting schema
 \dt core.*