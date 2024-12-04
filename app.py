from http.server import SimpleHTTPRequestHandler, HTTPServer

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<html><body><h1>Pavlo Suprun</h1></body></html>")

if __name__ == "__main__":
    server = HTTPServer(("localhost", 8000), MyHandler)
    server.serve_forever()
