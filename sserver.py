import BaseHTTPServer, SimpleHTTPServer
import ssl

class MyRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        log.info("do_GET")
        return SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

    def do_HEAD(self):
        log.info("do_GET")
        return SimpleHTTPServer.SimpleHTTPRequestHandler.do_HEAD(self)

if __name__ == "__main__":
    logging.basicConfig(
        format='[%(asctime)s][%(name)s][%(levelname)s] - %(message)s',
        datefmt='%Y-%d-%m %H:%M:%S',
        level=logging.DEBUG,
    )
    httpd = BaseHTTPServer.HTTPServer(('', 443), MyRequestHandler)
    httpd.socket = ssl.wrap_socket(httpd.socket, server_side=True, certfile='./cert.pem', keyfile='./cert.pem', ssl_version=ssl.PROTOCOL_TLSv1)
    httpd.serve_forever()
