from dotenv import load_dotenv
load_dotenv()

from scoring.pool import ScoringPool
from logger import log

def main():
    log.info("HCTF scoring server!")
    pool = ScoringPool()
    pool.watch()

if __name__ == "__main__":
    main()