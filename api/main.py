import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import fibonacci_api_handler

app = FastAPI()

origins = [
     os.getenv("ACSESS_ALLOW_URL"),  # フロントのオリジン
]

app.add_middleware(
    CORSMiddleware,
    #allow_origins=origins,  # 許可するオリジンのリスト
    allow_origins=["*"], # 全てのオリジンからのアクセスを許可
    allow_credentials=True,
    allow_methods=["*"],  # すべてのメソッドを許可
    allow_headers=["*"],  # すべてのヘッダーを許可
)

app.include_router(fibonacci_api_handler.router)