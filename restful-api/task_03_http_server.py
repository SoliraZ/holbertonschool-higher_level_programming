#!/usr/bin/python3
""" Task 03: Fetch and print posts from the API """
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class RequestHandler(BaseHTTPRequestHandler):
    """ A simple HTTP server that responds to GET requests """
    def send_text(self, data, status_code=200):
        self.send_response(status_code)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(data.encode("utf-8"))

    def send_json(self, data, status_code=200):
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

    def do_GET(self):
        if self.path == "/data":
            self.send_json({"name": "John", "age": 30, "city": "New York"})
        elif self.path == "/status":
            self.send_text("OK")
        elif self.path == "/info":
            self.send_json({
                "version": "1.0",
                "description": "A simple API built with http.server"
                })
        elif self.path == "/":
            self.send_text("Hello, this is a simple API!")
        else:
            self.send_text("Endpoint not found", 404)


if __name__ == "__main__":
    server_address = ("localhost", 8000)
    server = HTTPServer(server_address, RequestHandler)
    print("Serving on http://{}:{}".format(*server_address))
    server.serve_forever()
