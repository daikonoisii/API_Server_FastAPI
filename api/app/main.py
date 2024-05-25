import os
from typing import Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import fibonacci_api_handler

app = FastAPI()

# 環境変数から"アクセスを許可するオリジン"を取得
access_allow_urls:Optional[str] = os.getenv("ACSESS_ALLOW_URL")

if access_allow_urls:
    # セミコロンで区切られたパスをリストに変換
    origins:list[str] = access_allow_urls.split(';')
else:
    origins:list[None] = []

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # 許可するオリジンのリスト
    allow_credentials=True,
    allow_methods=["*"],  # すべてのメソッドを許可
    allow_headers=["*"],  # すべてのヘッダーを許可
)

app.include_router(fibonacci_api_handler.router)