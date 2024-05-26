from fastapi import APIRouter, Depends,HTTPException
from app.libs.math.fibonacci_number.generate_fibonacci_number import generate_fibonacci_number
from models import FibonacciResultModel,FibonacciValueModel

router = APIRouter()

@router.get("/fib")
def fibonacci_api_handler(input_value_model: FibonacciValueModel = Depends()) -> FibonacciResultModel:
    """
    指定された順番のフィボナッチ数を生成するルーター
    ex. n=1 -> 1, n=6 -> 8, n=7 -> 13 n=8 -> 21
    Args:
        input_value_model (FibonacciValueModel) : input_value_model.n
                                                    -> フィボナッチ数列の順番を指定する値.1で先頭のフィボナッチ数を指定する
    Returns:
        FibonacciResultModel(result = fibonacci_number) (FibonacciResultModel) : 指定された番目のフィボナッチ数
    Raises:
        HTTP_422_UNPROCESSABLE_ENTITY: リクエストの内容が不正 or フィボナッチ数を生成する関数が値を処理できなかった
        HTTP_500_INTERNAL_SERVER_ERROR: nが大きい際、再起的読み込みによって発生するエラー(スタックオーバーフロー等)
    """

    # n番目のフィボナッチ数を取得
    try:
        fibonacci_number:int = generate_fibonacci_number(input_value_model.n)
    except ValueError as e:
        # input_value_model.nが1以上の整数ではない
        raise HTTPException(status_code=422, detail=str(e))
    except RecursionError as e:
        # スタックオーバーフロー
        raise HTTPException(status_code=500, detail=str(e))

    return FibonacciResultModel(result = fibonacci_number)