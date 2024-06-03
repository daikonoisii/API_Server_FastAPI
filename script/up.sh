# api.env ファイルが存在しない場合にのみ新規作成
if [ ! -f api.env ]; then
    touch api.env
    echo 'LOG_FILE_NAME="api.log"' >> api.env
fi

docker-compose -f docker-compose.prod.yml build
docker compose -f docker-compose.prod.yml up -d