import pymysql
import env
from pymysql import Connection


class DB:
    @staticmethod
    def conn() -> Connection:
        return pymysql.connect(
            host=env.db_host,
            port=env.db_port,
            user=env.db_user,
            password=env.db_password,
            db=env.db_db,
            charset=env.db_charset
        )