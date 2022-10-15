export $(grep -v '^#' .env | xargs)

docker network create brick-query-app-network
# starts app database on localhost
docker run -d --net brick-query-app-network --name brick-query-app -p 127.0.0.1:5432:5432