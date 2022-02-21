from inspect import trace
import time

from db import DB
import env
from concurrent.futures import ThreadPoolExecutor
from logger import log
from scoring.scoring_system import ScoringSystem
from scoring.systems import escape_sql_enum_systems, get_scoring_systems

class ScoringPool:
    def __init__(self):
        self.executor: ThreadPoolExecutor = ThreadPoolExecutor(max_workers=env.scoring_thread_count)
        self.systems: list[ScoringSystem] = get_scoring_systems()
        self.eq_systems = escape_sql_enum_systems()

    def watch(self, interval: int or None = None) -> None:
        if interval == None: interval = env.fetch_interval
        interval: float = interval / 1000.0

        while True:
            start = time.time()
            status = self.compute()
            end = time.time()
            ti = end - start
            wait = interval - ti
            log.debug(f"pool compute {status} | Et {ti:.3f} sec, wait {max(0, wait)} sec")
            if wait > 0: time.sleep(wait)

    def compute(self) -> int:
        try:
            query = self.get_query()
            query_len = len(query)
            log.info(query_len)
            if query == None or query_len < 1: return 1
            return 0
        except Exception as e:
            log.critical(f"pool compute exception {e.__class__.__name__} {e}")
            return 2

    def get_query(self) -> list[int]:
        conn = DB.conn()
        cus = conn.cursor()
        cus.execute(f'''select `problem_scoring_id` from `problem_scoring` where (select `problem_type` from `problem_formats` where problem_formats.problem_format_id=problem_scoring.problem_format_id) in ({self.eq_systems})''')
        conn.close()
        return cus.fetchall()




        

