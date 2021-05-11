# #%L
# Speedtest and stats
# %%
from pprint import pprint
from typing import Any, Dict, List

import speedtest
from helpers.user import User

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

b_to_mb = lambda x: round(x / 1000_000, 2)

def main():
    speed_test: Dict[str, Any] = get_speed()
    machine = User()
    pprint(machine.get_dict())
    pprint(speed_test)
    print('Download: {0}\nUpload: {1}'.format(
        b_to_mb(speed_test['download']), b_to_mb(speed_test['upload'])
    ))


if __name__ == '__main__':
    main()
    # %%
