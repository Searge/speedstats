# #%L
# Speedtest and stats
# %%

from pprint import pprint
from typing import Any, Dict, List

import speedtest

st = speedtest.Speedtest()
servers: List[Dict] = st.get_closest_servers()
best_server: Dict[str, Any] = st.get_best_server()


def get_results() -> Dict:
    """
    Tying to get results.

    Returns
    -------
    Dict
        [str, Any]
    """

    st.get_best_server()

    st.download()
    st.upload()

    return st.results.dict()
# %%


def main():
    """[summary]."""
    pass


if __name__ == '__main__':
    pprint(get_results())
