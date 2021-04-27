import sqlite3

con = sqlite3.connect('speed.db')

cur = con.cursor()

# Create table
cur.execute(
    '''CREATE TABLE Client
               (UserID, Sponsor, Timestamp,
               Distance, Ping, Download, Upload,
               IP_Address)''')
cur.execute(
    '''CREATE TABLE Server
               (ServerID, Sponsor, Timestamp,
               Distance, Ping, Download, Upload,
               IP_Address)''')
cur.execute(
    '''CREATE TABLE Data
               (Timestamp, Ping, Download, Upload,
               bytes_received, bytes_sent)''')

tables = {'bytes_received': 105431322,
          'bytes_sent': 115326976,
          'download': 83765384.12075624,
          'upload': 91981785.83000948,
          'ping': 22.689,
          'share': None,
          'timestamp': '2021-04-21T15:13:59.646541Z',
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
          'server': {'cc': 'UA',
                     'country': 'Ukraine',
                     'd': 66.70811924428622,
                     'host': 'test.campus-rv.net:8080',
                     'id': '2558',
                     'lat': '50.6167',
                     'latency': 22.689,
                     'lon': '26.2500',
                     'name': 'Rivne',
                     'sponsor': 'Campus Networks',
                     'url': 'http://test.campus-rv.net:8080/speedtest/upload.php'
                     }}
Client = {'Country': tables['client']['country'],
          'ISP': tables['client']['isp'],
          'ISP_Rating': tables['client']['isprating'],
          'IP': tables['client']['ip'],
          'Latitude': tables['client']['lat'],
          'Longtitude': tables['client']['lon']}
