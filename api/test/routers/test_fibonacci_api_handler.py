from fastapi.testclient import TestClient
from fastapi import FastAPI
from app.routers.fibonacci_api_handler import router as fibonacci_router

app = FastAPI()
app.include_router(fibonacci_router)

client = TestClient(app)

def test_fibonacci_api_handler():
    """
    fibonacci_api_handlerのユニットテスト
    1以上の整数はフィボナッチ数を返すが、0以下の値や小数、文字列を渡すと422エラーが発生する
    """
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

    # 不正な値、0を渡したケース.422エラーが発生
    response = client.get("/fib?n=0")
    assert response.status_code == 422

    # 不正な値、小数を渡したケース.422エラーが発生
    response = client.get("/fib?n=1.1")
    assert response.status_code == 422

    # 不正な値、負の数を渡したケース.422エラーが発生
    response = client.get("/fib?n=-1")
    assert response.status_code == 422

    # 不正な値、文字列を渡したケース.422エラーが発生
    response = client.get("/fib?n=a")
    assert response.status_code == 422


