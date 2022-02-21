
import os


scoring_thread_count = int(os.environ.get('scoring_thread_count'))
fetch_interval = int(os.environ.get('fetch_interval'))
scoring_mode = os.environ.get('scoring_mode')

# db
db_host = os.environ.get('db_host')
db_port = int(os.environ.get('db_port'))
db_user = os.environ.get('db_user')
db_password = os.environ.get('db_password')
db_db = os.environ.get('db_db_name')
db_charset = os.environ.get('db_charset')