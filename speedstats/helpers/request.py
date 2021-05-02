from urllib3 import PoolManager, response
from urllib3.exceptions import HTTPError

# https://www.programcreek.com/python/example/106708/urllib3.exceptions.HTTPError
OK = 200


def http_error(status):
    match_status: dict = {
        200: 'OK',
        204: 'No Content',
        301: 'Moved Permanently',
        400: 'Bad Request',
        401: 'Unauthorized',
        402: 'Payment Required',
        403: 'Forbidden',
        404: 'Not Found',
        405: 'Method Not Allowed',
        406: 'Not Acceptable',
        407: 'Proxy Authentication Required',
        408: 'Request Timeout',
        500: 'Internal Server Error',
        501: 'Not Implemented',
        502: 'Bad Gateway',
        503: 'Service Unavailable',
        504: 'Gateway Timeout',
    }
    return match_status.get(status, f'Unknown status {status}')


def get_data(url: str) -> str:
    '''Simplify http requests & decoding data.

    TODO: Create Error handlers
    Args:
        url (str): Site address

    Returns:
        str: Dictionary in string
    '''
    http = PoolManager()
    request = http.request('GET', url)

    try:
        return request.data.decode()
    except HTTPError:
        print('Error', HTTPError)


if __name__ == '__main__':
    get_data('https://httpbin.org/status/404')