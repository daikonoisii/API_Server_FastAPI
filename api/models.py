from pydantic import BaseModel, Field

class FibonacciResultModel(BaseModel):
    """
    "フィボナッチ数を出力するAPI"の出力model.
    BaseModelで検証を行う.

    variable:
        result (int) : ある番目におけるフィボナッチ数.１以上の整数.
    """
    result: int = Field(..., gt=0)

    def __init__(self, **data):
        super().__init__(**data)

class FibonacciValueModel(BaseModel):
    """
    フィボナッチ数の番目を指定するmodel.
    BaseModelで検証を行う.

    variable:
        n (int) : フィボナッチ数の番目を指定する値.１以上の整数.
    """
    n: int = Field(..., gt=0)

    def __init__(self, **data):
        super().__init__(**data)
