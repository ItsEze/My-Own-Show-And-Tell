docker-compose up -d --build
# make sure the postgres container is ready, then run migrations
sleep 5
docker exec my-own-show-and-tell-api-1 python /src/manage.py makemigrations
docker exec my-own-show-and-tell-api-1 python /src/manage.py migrate