import pytest
from concurrent.futures import ThreadPoolExecutor
from app.libs.math.fibonacci_number.generate_fibonacci_number import generate_fibonacci_number

def test_generate_fibonacci_number():
    """
    generate_fibonacci_numberのユニットテスト.
    
    generate_fibonacci_number:
        Args:
            fibonacci_index (int) : フィボナッチ数列の順番を指定する値.1で先頭のフィボナッチ数を指定する.
        Returns:
            (int) : 指定された番目のフィボナッチ数.fibonacci_index = 0 の返り値は0.
        Raises:
            ValueError: フィボナッチ数のインデックスが有効範囲外 or インデックスが数値ではない
            RecursionError: スタックオーバーフロー
    """

    # 正常なケース
    assert generate_fibonacci_number(1) == 1  # 1番目のフィボナッチ数は1
    assert generate_fibonacci_number(2) == 1  # 2番目のフィボナッチ数は1
    assert generate_fibonacci_number(3) == 2  # 3番目のフィボナッチ数は2
    assert generate_fibonacci_number(4) == 3  # 4番目のフィボナッチ数は3
    assert generate_fibonacci_number(5) == 5  # 5番目のフィボナッチ数は5
    assert generate_fibonacci_number(6) == 8  # 6番目のフィボナッチ数は8
    assert generate_fibonacci_number(10) == 55  # 10番目のフィボナッチ数は55


    # 大きな値に対するテスト
    # assert generate_fibonacci_number(50) == 12586269025  # 50番目のフィボナッチ数は12586269025

    # 非常に大きな値のテスト
    # 注意: このテストは実行時間が長くなる可能性があるため、実際の環境に応じて実施
    # assert generate_fibonacci_number(99) == 218922995834555169026  # 99番目は218922995834555169026

    # エッジケース
    assert generate_fibonacci_number(0) == 0  # 0番目は0を返すべき


    # 異常なケース
    with pytest.raises(ValueError):  # 負の値に対してはValueErrorが発生
        generate_fibonacci_number(-1)

    with pytest.raises(ValueError):  # 文字列に対してはValueErrorが発生
        generate_fibonacci_number("1")

    with pytest.raises(ValueError):  #配列に対してはValueErrorが発生
        generate_fibonacci_number([1,2,3,4])

    with pytest.raises(ValueError):  # 浮動小数点数に対してはValueErrorが発生
        generate_fibonacci_number(1.1)

    with pytest.raises(ValueError):  # Noneに対してはValueErrorが発生
        generate_fibonacci_number(None)

    with pytest.raises(ValueError):   # 辞書に対してはValueErrorが発生
        generate_fibonacci_number({'index': 1})

    with pytest.raises(ValueError):   # タプルに対してはValueErrorが発生
        generate_fibonacci_number((1,))
        
    with pytest.raises(ValueError):   # オブジェクト型
        generate_fibonacci_number(object())
    
    with pytest.raises(RecursionError): # 極端に大きな値
        generate_fibonacci_number(1000000)

    with pytest.raises(ValueError):   # 非常に大きな文字列
        generate_fibonacci_number("very long string" * 100000)
