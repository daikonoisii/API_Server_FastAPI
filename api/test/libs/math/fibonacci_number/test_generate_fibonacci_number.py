import pytest
from app.libs.math.fibonacci_number.generate_fibonacci_number import generate_fibonacci_number

def test_generate_fibonacci_number():
    """
    generate_fibonacci_numberのユニットテスト.
    1以上の整数に対してはその番目のフィボナッチ数が返ってくる.0以下に対しては0が返ってくる.
    """
    # 正常なケース
    assert generate_fibonacci_number(1) == 1  # 1番目のフィボナッチ数は1
    assert generate_fibonacci_number(2) == 1  # 2番目のフィボナッチ数は1
    assert generate_fibonacci_number(3) == 2  # 3番目のフィボナッチ数は2
    assert generate_fibonacci_number(4) == 3  # 4番目のフィボナッチ数は3
    assert generate_fibonacci_number(5) == 5  # 5番目のフィボナッチ数は5
    assert generate_fibonacci_number(6) == 8  # 6番目のフィボナッチ数は8
    assert generate_fibonacci_number(10) == 55  # 10番目のフィボナッチ数は55

    # エッジケース
    assert generate_fibonacci_number(0) == 0  # 0番目は0を返すべき

    # 異常なケース
    with pytest.raises(ValueError):  # 負の値に対してはValueErrorが発生
        generate_fibonacci_number(-1)
    with pytest.raises(ValueError):  # 文字列に対してはValueErrorが発生
        generate_fibonacci_number("a")
    with pytest.raises(ValueError):  #配列に対してはValueErrorが発生
        generate_fibonacci_number([1,2,3,4])
        