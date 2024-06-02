# Web
デプロイ用ファイルを配置

## Description
CloudFlare　tunnelの設定ファイルを配置する

## File Structure

```
.
├── README.md
└── prod
    ├── {トンネルID}.json
    ├── cert.pem
    └── config.yaml
```

- ``README.md`` :   
    　プロジェクトの説明、セットアップ手順、使用方法などを記載するドキュメント  

- ``prod/``  
　デプロイに使用する設定ファイルを格納するディレクトリ  
  - `` {トンネルID}.json``  
  　CloudFlare　tunnelに関連付けられた認証情報  
  - ``cert.pem``  
  　CloudFlareの証明書  
  ``config.yaml``  
  　CloudFlare　tunnelの設定  
