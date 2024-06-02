
# fib_api
フィボナッチ数を返すAPI

## Description
APIサーバー

URL：https://api.dishizawa.net

フィボナッチ数を返すAPI

URL：https://api.dishizawa.net/fib

クエリ：
- n (int): フィボナッチ数の番目を指定する値


## Installation

必要なソフトウェアやライブラリのインストール方法

```bash
docker compose -f docker-compose.prod.yml build

docker compose -f docker-compose.prod.yml up -d
```

### Deletion

```bash
docker compose -f docker-compose.prod.yml down
```

### Use Script

Installtionをまとめて実行

```bash
$ bash ./script/up.sh
```

Deletionを実行

```bash
$ bash ./script/down.sh
```

### Use API

case: 120番目のフィボナッチ数を取得

URL：https://api.dishizawa.net/fib?n=120

return:
```
{
  "result": 5.358359254990966e+24
}
```
Script: `curl -X GET -H "Content-Type: application/json" "https://api.dishizawa.net/fib?n=120"`

return:
```
{
  "result":5358359254990966640871840
}
```

## File Structure
```
.
├── README.md
├── api
│   ├── README.md
│   ├── api.Dockerfile
│   ├── app
│   │   ├── __init__.py
│   │   ├── libs
│   │   │   └── math
│   │   │       └── fibonacci_number
│   │   │           ├── generate_fibonacci_number.py
│   │   │           └── validate_fibonacci.py
│   │   ├── main.py
│   │   └── routers
│   │       └── fibonacci_api_handler.py
│   ├── models.py
│   ├── requirements.txt
│   └── test
│       ├── libs
│       │   └── math
│       │       └── fibonacci_number
│       │           ├── test_generate_fibonacci_number.py
│       │           └── test_validate_fibonacci.py
│       └── routers
│           └── test_fibonacci_api_handler.py
├── api.env
├── docker-compose.prod.yml
├── docker-compose.yml
├── script
│   ├── down.sh
│   └── up.sh
└── web
    ├── README.md
    └── prod
        ├── {トンネルID}.json
        ├── cert.pem
        └── config.yaml

```

- `api/`

  - FastAPIを使用したAPIサーバー

- `web/`

  - APIサーバーを公開するための設定.cloudflare tunnelを利用

- `api.env`

  - `api/`で使用される環境変数を記述

- `script/`

  - インストールやコンテナの操作を行うシェルスクリプト

- `docker-compose.yml`
  - 複数のコンテナを定義し、実行するための設定.開発用

- `docker-compose.prod.yml`
  - 複数のコンテナを定義し、実行するための設定.本番用
