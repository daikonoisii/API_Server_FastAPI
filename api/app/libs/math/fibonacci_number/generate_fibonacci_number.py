def generate_fibonacci_number(fibonacci_index:int):
    """
    指定された順番のフィボナッチ数を生成する関数
    ex. n=1 -> 1, n=5 -> 8, n=6 -> 13 n=7 -> 21
    Args:
        fibonacci_index (int) : single_value_model.value
                                                -> フィボナッチ数列の順番を指定する値.1で先頭のフィボナッチ数を指定する
    Returns:
        generate_fibonacci_number(fibonacci_index -1) + generate_fibonacci_number(fibonacci_index -2) (int) : 指定された番目のフィボナッチ数
    Raises:
        HTTP_400_BAD_REQUEST:
    """

    # フィボナッチ数を計算
    # n番目のフィボナッチ数はn-1番目とn-2番目を足したものであり、1番目のフィボナッチ数は1,0番目以下は0とすることで値が収束する
    if fibonacci_index <= 0:
        return 0
    elif fibonacci_index == 1:
        return 1
    else:
        return generate_fibonacci_number(fibonacci_index -1) + generate_fibonacci_number(fibonacci_index -2)
