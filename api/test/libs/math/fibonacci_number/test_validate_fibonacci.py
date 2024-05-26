import pytest
from app.libs.math.fibonacci_number.validate_fibonacci import fib_index

def test_fib_index():
    """
    validate_fibonacci.fib_indexのユニットテスト

    fib_index:
        Args:
            index (int): フィボナッチ数列のインデックス
        Returns:
            (bool): indexが0以上の整数であればTrue、そうでなければFalse
    """
    # 正常なケース
    assert fib_index(1) == True  # 1以上の整数
    assert fib_index(10) == True  # 1以上の整数

    # エッジケース
    assert fib_index(0) == True

    # 異常なケース
    assert fib_index(-1) == False # 負の数
    assert fib_index(1.1) == False # 浮動少数
    assert fib_index("1") == False # 文字列
    assert fib_index("very long string" * 10000) == False # 非常に大きな文字列
    assert fib_index(None) == False # None
    assert fib_index([1]) == False # リスト
    assert fib_index({'index': 1}) == False # 辞書
    assert fib_index((5,)) == False # タプル
    assert fib_index(object()) == False # オブジェクト

