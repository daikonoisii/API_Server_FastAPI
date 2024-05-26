from app.libs.math.fibonacci_number import validate_fibonacci

def generate_fibonacci_number(fibonacci_index:int):
    """
    指定された順番のフィボナッチ数を生成する関数
    ex. n=1 -> 1, n=5 -> 8, n=6 -> 13 n=7 -> 21
    Args:
        fibonacci_index (int) : フィボナッチ数列の順番を指定する値.1で先頭のフィボナッチ数を指定する.
    Returns:
        (int) : 指定された番目のフィボナッチ数.fibonacci_index = 0 の返り値は0.
    Raises:
        ValueError: フィボナッチ数のインデックスが有効範囲外 or インデックスが数値ではない
        RecursionError: スタックオーバーフロー
    """

    # フィボナッチ数の番数が不正な値でなはないか検証
    if not validate_fibonacci.fib_index(fibonacci_index):
        raise ValueError("Invalid index for Fibonacci number")

    # フィボナッチ数を計算
    # n番目のフィボナッチ数はn-1番目とn-2番目を足したものであり、1番目のフィボナッチ数は1,0番目以下は0とすることで値が収束する
    if fibonacci_index <= 0:
        return 0
    elif fibonacci_index == 1:
        return 1
    else:
        return generate_fibonacci_number(fibonacci_index -1) + generate_fibonacci_number(fibonacci_index -2)
