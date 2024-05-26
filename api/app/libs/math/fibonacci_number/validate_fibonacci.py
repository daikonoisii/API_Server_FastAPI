def fib_index(index: int) -> bool:
    """
    フィボナッチ数のindexが不正ではないか検証
    本来、index=0は存在しないが、generate_fibonacci_numberは計算にindex=0を使用するため、0を許可
    Args:
        index (int): フィボナッチ数列のインデックス
    Returns:
        (bool): indexが0以上の整数であればTrue、そうでなければFalse
    """

    # 0以上の整数ならTrue,0未満 or 整数ではない場合はFalse
    if isinstance(index, int) and index >= 0:
        return True
    else:
        return False