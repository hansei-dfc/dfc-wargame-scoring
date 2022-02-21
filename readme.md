## .env **needs** to be created

```
scoring_thread_count=10 # 동시 채점 수
fetch_interval=1500 # ms
scoring_mode=find_flag,baekjoon

db_host=[db host]
db_port=3306
db_user=[ex) root]
db_password=
db_db_name=
db_charset=utf8

```


## Necessary Python Packages
```
PyMySQL
python-dotenv
```

### installation
```
pip install -r requirements.txt
```