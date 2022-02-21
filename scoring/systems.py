from scoring.scoring_system import ScoringSystem
from scoring.system.find_flag import FindFlagSystem

import env
from logger import log

def get_scoring_systems() -> list[ScoringSystem]:
    syss = []
    for mod in env.scoring_mode.split(','):
        mod = mod.strip()
        sys = scoring_systems.get(mod)
        
        if sys == None: 
            log.warning(f'{mod} can not be found')
            continue

        syss.append(sys)
    return syss

def escape_sql_enum_systems():
    query = ''
    for i, mod in enumerate(env.scoring_mode.split(',')):
        query += f"{',' if i > 0 else ''}'{mod.strip()}'"
    return query

scoring_systems: dict[ScoringSystem] = {
    'find_flag': type(FindFlagSystem)
}