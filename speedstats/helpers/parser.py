from xml.dom import minidom
from urllib3 import PoolManager


def get_data(url: str) -> str:
    """Simplify http requests & decoding data.

    TODO: Create Error handlers
    Args:
        url (str): Site address

    Returns:
        str: Dictionary in string
    """
    http = PoolManager()
    request = http.request('GET', url)
    return request.data.decode()


def parse(url: str):
    dat = minidom.parseString(get_data(url))
    servers = dat.getElementsByTagName('server')

    title = [
            'ID', 'Host', 'Sponsor', 'Latitude', 'Longtitude', 'City', 'Country'
            ]
    with open('speedstats/db/speedservers.csv', 'w') as csv:
        csv.write(",".join(title) + "\n")
        for server in servers:
            csv.write(",".join([
                server.attributes['id'].value,
                server.attributes['host'].value,
                server.attributes['sponsor'].value,
                server.attributes['lat'].value,
                server.attributes['lon'].value,
                server.attributes['name'].value,
                server.attributes['cc'].value
            ]) + "\n")


if __name__ == '__main__':
    URL = 'http://c.speedtest.net/speedtest-servers.php'
    parse(URL)
