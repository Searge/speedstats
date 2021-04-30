# %%
"""Create unique user id.

Find machine name, city location and UUID
"""
import json
import platform
from uuid import uuid4

from urllib3 import PoolManager


class User(object):
    """Gethering information about user machine & ISP."""
    # TODO: Create object if not exists

    def __init__(self):
        """Construct user id."""
        self.uid = uuid4()
        self.hostname = platform.node().title()

        loc = self.get_location()
        self.city, self.country = self.get_place(*loc)

        self.name = self.get_name(self.uid, self.hostname, self.city)

    def __repr__(self) -> str:
        """Give a name.

        Returns:
            str: Machine name
        """
        return self.name

    def get_data(self, url: str) -> str:
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

    def get_location(self) -> tuple:
        """Find the ISP latitude, longtitude.

        Returns:
            tuple: (longtitude, latitude)
        """
        url = 'http://ipinfo.io/loc'
        return tuple(self.get_data(url).rstrip().split(','))

    def get_place(self, lat: float, lon: float) -> tuple:
        """Unpack dictionary and get the city, contry.

        Args:
            lat (float): longtitude
            lon (float): latitude

        Returns:
            tuple: City, Country code
        """
        url = ('http://nominatim.openstreetmap.org/reverse'
               '?format=json&accept-language=en&zoom=12&addressdetails=1'
               '&lat={0}&lon={1}'.format(lat, lon))
        addresses: dict = json.loads(self.get_data(url))

        city = addresses['address']['city']
        country_code = addresses['address']['country_code'].upper()
        return (city, country_code)

    def get_name(self, uid: str, hostname: str, city: str) -> str:
        """Choose some name variants.

        Args:
            uid: str
            machine: str
            city: str

        Returns:
            str: The choosen one!
        """
        variants = {
            1: hostname,
            2: '{0}_{1}'.format(hostname, city),
            3: '{0}_{1}'.format(hostname, uid),
            4: 'Write your own.',
        }
        for num, variant in variants.items():
            print(num, variant)

        number = int(input('Choose machine name: '))
        if number == 4:
            variants[4] = input('Your name: ')

        return variants.get(number)

    def get_dict(self):
        return self.__dict__
# %%


if __name__ == '__main__':
    laptop = User()
    print(laptop.__dict__)
