import logging
import json
from fastapi import Request ,HTTPException
from fastapi.responses import JSONResponse
from starlette.responses import JSONResponse, StreamingResponse

# ロギングの設定
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s',filename='app.log',filemode='a')

async def log_http_requests(request: Request, call_next):
    """
    ミドルウェアとして機能する非同期関数.すべてのHTTPリクエストとレスポンスをログに記録する.
    
    Args:
        request (Request): FastAPIによって受け取られるリクエストオブジェクト
        call_next: リクエストオブジェクトを受け取り、次のリクエスト処理関数またはミドルウェアを呼び出すコールバック関数

    Returns:
        response: 処理後のレスポンスオブジェクト
    """
    # リクエストの受信をログに記録
    logging.info(f"New request: {request.method} {request.url}")
    try:
        # 次のリクエストハンドラを非同期で呼び出し、レスポンスを待機
        response = await call_next(request)
        
        if response.status_code == 422:
            content = []
            async for chunk in response.body_iterator:
                content.append(chunk)
            # JSONとしてデコード
            details = json.loads(b''.join(content).decode())
            # 'detail' キーからエラー詳細を取得しログに記録
            error_details = details['detail']
            logging.error(f"Error details: {error_details}")
            # ステータスコードも元のレスポンスから取得して設定
            response = StreamingResponse(iter(content), status_code=response.status_code, media_type=response.media_type)

    except Exception as e:
        # 例外が発生した場合はエラーをログに記録し、500エラーを生成
        logging.error(f"Message: {str(e)}")
        response = JSONResponse(status_code=500, content={"Message": "Server Error"})

    finally:
        # 最終的なレスポンスステータスをログに記録
        logging.info(f"Response status: {response.status_code}")

        return response
