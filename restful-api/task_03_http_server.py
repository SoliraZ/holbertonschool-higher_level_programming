#!/usr/bin/python3
""" Task 03: Fetch and print posts from the API """
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class RequestHandler(BaseHTTPRequestHandler):
    """ A simple HTTP server that responds to GET requests """
    def do_GET(self):
        if self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            json_data = json.dumps(data)
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json_data.encode("utf-8"))
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")
        elif self.path == "/info":
            info = {"version": "1.0", "description": "A simple API"}
            json_info = json.dumps(info)
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(json_info.encode("utf-8"))
        elif self.path == "/":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        else:
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(b"404 Not Found")


host = "localhost"
port = 8000

server = HTTPServer((host, port), RequestHandler)
print(f"Serving on http://{host}:{port}")

server.serve_forever()
