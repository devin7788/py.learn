from tornado import httpclient, ioloop
from tornado.httpclient import AsyncHTTPClient

url = 'http://127.0.0.1:8888/'

def make_client():
    http_client = httpclient.HTTPClient()
    try:
        response = http_client.fetch(url)
        print(response.body)
    except httpclient.HTTPError as e:
        # HTTPError is raised for non-200 responses; the response
        # can be found in e.response.
        print("Error: " + str(e))
    except Exception as e:
        # Other errors are possible, such as IOError.
        print("Error: " + str(e))
    http_client.close()

async def test():
    http_client = AsyncHTTPClient()
    result = await http_client.fetch(url)
    print(result.body)


if __name__ == "__main__":
    # make_client()
    io_loop = ioloop.IOLoop.current()
    io_loop.run_sync(test)
