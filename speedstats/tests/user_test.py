import json
from urllib3 import PoolManager


def get_data(url: str) -> str:
    """Simplify http requests & decoding data.

    Args:
        url (str): Site address

    Returns:
        str: Dictionary in string
    """
    http = PoolManager()
    request = http.request('GET', url)
    return request.data.decode()


def get_location() -> tuple:
    """Find the ISP latitude, longtitude.

    Returns:
        tuple: (longtitude, latitude)
    """
    url = 'http://ipinfo.io/loc'
    return tuple(get_data(url).rstrip().split(','))


def get_place(lat: float, lon: float) -> tuple:
    """Unpack dictionary and get the city, contry.

    Args:
        lat (float): longtitude
        lon (float): latitude

    Returns:
        tuple: City, Country code
    """
    url = ('http://nominatim.openstreetmap.org/reverse'
            '?format=json&accept-language=en&zoom=10&addressdetails=1'
            '&lat={0}&lon={1}'.format(lat, lon))
    addresses: dict = json.loads(get_data(url))

    city = addresses['address']['city']
    country_code = addresses['address']['country_code'].upper()
    return (city, country_code)


if __name__ == '__main__':
    loc = get_location()
    city, country = get_place(*loc)
    print(city, country)