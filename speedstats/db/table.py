import sqlite3

con = sqlite3.connect('speed.db')

cur = con.cursor()

# Create table
cur.execute(
    '''CREATE TABLE Client
               (UserID, Sponsor, Timestamp,
               Distance, Ping, Download, Upload,
               IP_Address)''')

#  Answer from function
user = {
    'uid': '86e9661c4c2f',
    'hostname': 'Raspberry-Pi',
    'name': 'Raspberry Pi',
    'city': 'Lutsk',
    'country': 'UA',
    }

speedtest = {'bytes_received': 112691192,
             'bytes_sent': 117481472,
             'client': {'country': 'UA',
                        'ip': '134.249.159.131',
                        'isp': 'Kyivstar',
                        'ispdlavg': '0',
                        'isprating': '3.7',
                        'ispulavg': '0',
                        'lat': '50.7614',
                        'loggedin': '0',
                        'lon': '25.331',
                        'rating': '0'},
             'download': 89982120.51067148,
             'ping': 21.183,
             'server': {'cc': 'UA',
                        'country': 'Ukraine',
                        'd': 66.70811924428622,
                        'host': 'test.campus-rv.net:8080',
                        'id': '2558',
                        'lat': '50.6167',
                        'latency': 21.183,
                        'lon': '26.2500',
                        'name': 'Rivne',
                        'sponsor': 'Campus Networks',
                        'url': 'http://test.campus-rv.net:8080/speedtest/upload.php'},
             'share': None,
             'timestamp': '2021-05-01T13:27:34.581942Z',
             'upload': 93695796.2779435}

Client = {'Country': speedtest['client']['country'],
          'ISP': speedtest['client']['isp'],
          'ISP_Rating': speedtest['client']['isprating'],
          'IP': speedtest['client']['ip'],
          'Latitude': speedtest['client']['lat'],
          'Longtitude': speedtest['client']['lon']}
