import signal
import time

from tornado import httpclient
from tornado.httpclient import AsyncHTTPClient


def make_client():
    http_client = httpclient.HTTPClient()
    try:
        response = http_client.fetch("http://127.0.0.1:8888/")
        print(response.body)
    except httpclient.HTTPError as e:
        # HTTPError is raised for non-200 responses; the response
        # can be found in e.response.
        print("Error: " + str(e))
    except Exception as e:
        # Other errors are possible, such as IOError.
        print("Error: " + str(e))
    http_client.close()


if __name__ == "__main__":
    make_client()
