# #%L
# Speedtest and stats
# %%
from pprint import pprint
from typing import Any, Dict, List
from helpers.user import User

import speedtest

speed = speedtest.Speedtest()


def get_speed() -> Dict:
    """
    Tying to get results.

    Returns
    -------
    Dict
        [str, Any]
    """
    servers: List[Dict] = speed.get_closest_servers()
    speed.get_best_server(servers)

    speed.download()
    speed.upload()

    return speed.results.dict()


def main():
    speed_test: Dict[str, Any] = get_speed()
    machine = User()
    pprint(machine.get_dict())
    pprint(speed_test)


if __name__ == '__main__':
    main()
    # %%
