import os
import pytest
import asyncio
from app.main import app
from httpx import AsyncClient
from fastapi.testclient import TestClient
from app.routers.fibonacci_api_handler import router as fibonacci_router

app.include_router(fibonacci_router)

client = TestClient(app)


# 環境変数からlogファイルの名称を取得
API_SERVER_NAME:str = os.getenv('API_SERVER_NAME', "http://localhost:9004/")

@pytest.mark.asyncio
async def test_fibonacci_api_handler_concurrent_stress():
    """
    fibonacci_api_handlerの負荷テスト(並行処理)

    fibonacci_api_handler:
        Args:
            input_value_model (FibonacciValueModel) : input_value_model.n
                                                        -> フィボナッチ数列の順番を指定する値.1で先頭のフィボナッチ数を指定する
        Returns:
            FibonacciResultModel(result = fibonacci_number) (FibonacciResultModel) : 指定された番目のフィボナッチ数
        Raises:
            HTTP_422_UNPROCESSABLE_ENTITY: リクエストの内容が不正
    """
    # 非同期に100回りクエストを送信
    async with AsyncClient(base_url=API_SERVER_NAME) as ac:
        # 同時に100回リクエスト
        tasks:list = [ac.get("/fib?n=100") for _ in range(100)]
        responses = await asyncio.gather(*tasks)
        assert all(response.status_code == 200 for response in responses)


def test_fibonacci_api_handler_value():
    """
    fibonacci_api_handlerのユニットテスト

    fibonacci_api_handler:
        Args:
            input_value_model (FibonacciValueModel) : input_value_model.n
                                                        -> フィボナッチ数列の順番を指定する値.1で先頭のフィボナッチ数を指定する
        Returns:
            FibonacciResultModel(result = fibonacci_number) (FibonacciResultModel) : 指定された番目のフィボナッチ数
        Raises:
            HTTP_422_UNPROCESSABLE_ENTITY: リクエストの内容が不正
    """
    # 正常なケース

    # 1番目のフィボナッチ数は1
    response = client.get("/fib?n=1")
    assert response.status_code == 200
    assert response.json() == {"result": 1}

    # 5番目のフィボナッチ数は5
    response = client.get("/fib?n=5")
    assert response.status_code == 200
    assert response.json() == {"result": 5}

    # 10番目のフィボナッチ数は55
    response = client.get("/fib?n=10")
    assert response.status_code == 200
    assert response.json() == {"result": 55}

    # 大きな値のテスト
    # 注意: このテストは実行時間が長くなる可能性があるため、実際の環境に応じて実施
    response = client.get("/fib?n=99")
    assert response.status_code == 200
    assert response.json() == {"result": 218922995834555169026}
    
    response = client.get("/fib?n=500")
    assert response.status_code == 200
    assert response.json() == {"result":139423224561697880139724382870407283950070256587697307264108962948325571622863290691557658876222521294125}


    # 異常なケース

    # 不正な値、負の数を渡したケース.422エラーを期待
    response = client.get("/fib?n=-1")
    assert response.status_code == 422

    # 不正な値、文字列を渡したケース.422エラーを期待
    response = client.get("/fib?n=a")
    assert response.status_code == 422

    # 不正な値、小数を渡したケース.422エラーを期待
    response = client.get("/fib?n=1.1")
    assert response.status_code == 422

    # 不正な値、0を渡したケース.422エラーを期待
    response = client.get("/fib?n=0")
    assert response.status_code == 422

    # 空文字を渡したケース、422エラーを期待
    response = client.get("/fib?n=")
    assert response.status_code == 422

    # 特殊文字を渡したケース、422エラーを期待
    response = client.get("/fib?n=%")
    assert response.status_code == 422

    # 誤ったパラメータ名を使用したケース、422エラーを期待
    response = client.get("/fib?num=10")
    assert response.status_code == 422

    # 非常に大きな文字列を渡したケース、422エラーを期待
    response = client.get("/fib?n="+"very_long_string" * 4000)
    assert response.status_code == 422