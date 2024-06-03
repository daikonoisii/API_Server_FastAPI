# api
APIサーバー

## Description
APIサーバー

URL：https://api.dishizawa.net

- フィボナッチ数を返すAPI

    URL：https://api.dishizawa.net/fib

    クエリ：
  - n (int): フィボナッチ数の番目を指定する値

## API

- ``/fib`` :

    指定された順番のフィボナッチ数を生成するルーター
    ex. n=1 -> 1, n=6 -> 8, n=7 -> 13 n=8 -> 21

    Args:  
    　　``n`` (int): フィボナッチ数列の順番を指定する値.1で先頭のフィボナッチ数を指定する  

    Returns:  
    　　``result`` (int): 指定された番目のフィボナッチ数  

    Raises:  
        HTTP_422_UNPROCESSABLE_ENTITY: リクエストの内容が不正 or フィボナッチ数を生成する関数が値を処理できなかった

### Usage
case: 120番目のフィボナッチ数を取得

URL：https://api.dishizawa.net/fib?n=120

return:
```
{"result":5358359254990966640871840}
```
Script: `curl -X GET -H "Content-Type: application/json" "https://api.dishizawa.net/fib?n=120"`

return:
```
{
  "result":5358359254990966640871840
}
```

## Test
`api/test/`で以下のコマンドを実行することでtestを行うことができる。
```
% pytest
```

## File Structure
```
.
├── README.md
├── api.Dockerfile
├── app
│   ├── __init__.py
│   ├── libs
│   │   ├── math
│   │   │   └── fibonacci_number
│   │   │       ├── generate_fibonacci_number.py
│   │   │       └── validate_fibonacci.py
│   │   └── utils
│   │       └── logger.py
│   ├── main.py
│   └── routers
│       └── fibonacci_api_handler.py
├── models.py
├── requirements.txt
└── test
    ├── libs
    │   └── math
    │       └── fibonacci_number
    │           ├── test_generate_fibonacci_number.py
    │           └── test_validate_fibonacci.py
    └── routers
        └── test_fibonacci_api_handler.py


```
- ``README.md`` :   
    　プロジェクトの説明、セットアップ手順、使用方法などを記載するドキュメント  

- ``api.Dockerfile`` :   
    　api Dockerコンテナのイメージを作成するための指示書  

- ``app`` :   
    　アプリケーションの主要なコード  
    - ``__init__.py``:   
    　appディレクトリをPythonパッケージとして認識させるためのファイル
    - ``libs/``:  
    　ライブラリやユーティリティ関数を格納するディレクトリ
      - ``math/``  
      　数学関連のライブラリを格納するディレクトリ
        - ``fibonacci_number/``:  
        　フィボナッチ数に関連するライブラリを格納するディレクトリ
          - ``generate_fibonacci_number.py``  
          　フィボナッチ数を生成する関数を含むファイル
          - ``validate_fibonacci.py``  
          　フィボナッチ数のバリデーションを行う関数を含むファイル
      - ``utils``:  
        　汎用関数を記述
        - ``logger.py``:  
          　logger関数を含むファイル
    - ``main.py`` :   
    　アプリケーションのエントリーポイント  
    　FastAPIのインスタンスを作成  
    - ``routers/``:  
    　APIエントリーポイントを定義するディレクトリ
      - ``fibonacci_api_handler.py``  
       フィボナッチ数に関連するAPIのルーター


- ``models.py``:   
    　APIリクエストとレスポンスのPydanticモデル  

- ``requirements.txt`` :   
  　　　pipでインストールするライブラリ一覧  

- ``test/`` :   
    　app内のモジュールのテスト
    - ``libs/``  
    　`app/libs`ディレクトリ内のライブラリをテストするためのテストコードを格納するディレクトリ
      - ``math/``  
        - ``fibonacci_number``
          - ``test_generate_fibonacci_number.py``  
        　`generate_fibonacci_number.py`のテスト
          -  ``test_validate_fibonacci.py``  
        　`test_validate_fibonacci.py`のテスト
    - ``routers``  
    　`app/routers`ディレクトリ内のAPIエンドポイントをテストするためのテストコードを格納するディレクトリ
      - ``test_fibonacci_api_handler.py``  
       `fibonacci_api_handler.py`のテスト
