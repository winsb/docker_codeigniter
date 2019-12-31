# docker_codeigniter
## 概要
dockerでPHP(Apache)+MySQL+phpMyAdminを構築し、  
CodeIgniterのファイルを設定する。  
※ローカル環境専用

## 構築環境
- PHP7.2-apache
- CodeIgniter3.1.10
- MySQL5.7
- phpMyAdmin5

## 動作環境
- Docker for Windows 2.1.0.5
- python 3.5.1

## 使い方

### 準備
```
python init.py
docker-compose build --no-cache
```

### 起動
```
doucker-compose up -d
```

### アクセス（動作確認）
CodeIgniter

- http://localhost/
- http://localhost/welcome/index

phpMyAdmin

- http://localhost:8080/

### 編集
./htmlディレクトリ内のファイルを編集する。  
CodeIgniterの使い方は[CodeIgniter](http://codeigniter.jp/)を参照してください。

### 停止
```
doucker-compose down
```

## 注意
- ローカル環境を前提に構築しているため、セキュリティなどを考慮していません。
- buildなどで失敗する場合はDockerやWindowsの設定を確認してください。

## 参考
- http://codeigniter.jp/
- https://qiita.com/ayato/items/4a620928160db02f302c
- https://qiita.com/nemui_/items/f911be7ffa4f29293fd5
- https://qiita.com/furu8ma/items/50718efebee20fd24517
- http://www.ci-guide.info
- http://onocom.net/blog/category/programing/framework/codeigniter/
- https://blog.magcho.com/dockerで立ち上げたwebサーバでmod_rewriteしたかった話/