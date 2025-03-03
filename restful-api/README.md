# 🌐 RESTful API

This repository contains various Python scripts that demonstrate the creation and consumption of RESTful APIs using different tools and libraries.

## 📋 Tasks

### 0. 🌐 HTTP vs HTTPS
Understand the differences between HTTP and HTTPS, the structure of HTTP requests and responses, and common HTTP methods and status codes.

- **Instructions:**
  - Differentiate between HTTP and HTTPS.
  - Understand the structure of HTTP requests and responses.
  - Explore common HTTP methods and status codes.

### 1. 🛠️ Consume data from an API using command line tools (curl)
Learn to use `curl` to interact with APIs from the command line.

- **File:** `task_01_curl.sh`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat task_01_curl.sh 
    #!/bin/bash
    curl --version
    curl http://example.com
    curl https://jsonplaceholder.typicode.com/posts
    curl -I https://jsonplaceholder.typicode.com/posts
    curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts

    user@ubuntu:~/$ ./task_01_curl.sh
    ```

### 2. 🐍 Consuming and processing data from an API using Python
Use Python's `requests` library to fetch and process data from an API.

- **File:** `task_02_requests.py`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat main_02_requests.py 
    #!/usr/bin/env python3
    from task_02_requests import fetch_and_print_posts, fetch_and_save_posts

    fetch_and_print_posts()
    fetch_and_save_posts()

    user@ubuntu:~/$ ./main_02_requests.py 
    ```

### 3. 🌐 Develop a simple API using Python with the `http.server` module
Set up a basic web server using Python's `http.server` module and handle different types of HTTP requests.

- **File:** `task_03_http_server.py`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat task_03_http_server.py 
    #!/usr/bin/env python3
    from http.server import BaseHTTPRequestHandler, HTTPServer
    import json

    class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            if self.path == '/':
                self.send_response(200)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(b'Hello, this is a simple API!')
            elif self.path == '/data':
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                data = {"name": "John", "age": 30, "city": "New York"}
                self.wfile.write(json.dumps(data).encode())
            else:
                self.send_response(404)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(b'Endpoint not found')

    def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
        server_address = ('', port)
        httpd = server_class(server_address, handler_class)
        print(f'Starting httpd server on port {port}')
        httpd.serve_forever()

    if __name__ == "__main__":
        run()

    user@ubuntu:~/$ ./task_03_http_server.py 
    ```

### 4. 🐍 Develop a Simple API using Python with Flask
Create a RESTful API using the Flask framework.

- **File:** `task_04_flask.py`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat task_04_flask.py 
    #!/usr/bin/env python3
    from flask import Flask, jsonify, request

    app = Flask(__name__)

    users = {
        "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
        "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
    }

    @app.route('/')
    def home():
        return "Welcome to the Flask API!"

    @app.route('/data')
    def data():
        return jsonify(list(users.keys()))

    @app.route('/status')
    def status():
        return "OK"

    @app.route('/users/<username>')
    def get_user(username):
        user = users.get(username)
        if user:
            return jsonify(user)
        else:
            return jsonify({"error": "User not found"}), 404

    @app.route('/add_user', methods=['POST'])
    def add_user():
        data = request.get_json()
        username = data.get('username')
        if not username:
            return jsonify({"error": "Username is required"}), 400
        users[username] = data
        return jsonify({"message": "User added", "user": data}), 201

    if __name__ == "__main__":
        app.run()

    user@ubuntu:~/$ flask --app task_04_flask.py run
    ```

### 5. 🔒 API Security and Authentication Techniques
Implement basic and token-based authentication to secure your API.

- **File:** `task_05_basic_security.py`
- **Usage:**
    ```sh
    user@ubuntu:~/$ cat task_05_basic_security.py 
    #!/usr/bin/env python3
    from flask import Flask, jsonify, request
    from flask_httpauth import HTTPBasicAuth
    from werkzeug.security import generate_password_hash, check_password_hash
    from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

    app = Flask(__name__)
    auth = HTTPBasicAuth()
    app.config['JWT_SECRET_KEY'] = 'super-secret'
    jwt = JWTManager(app)

    users = {
        "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
        "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
    }

    @auth.verify_password
    def verify_password(username, password):
        user = users.get(username)
        if user and check_password_hash(user['password'], password):
            return user

    @app.route('/basic-protected')
    @auth.login_required
    def basic_protected():
        return "Basic Auth: Access Granted"

    @app.route('/login', methods=['POST'])
    def login():
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        user = users.get(username)
        if user and check_password_hash(user['password'], password):
            access_token = create_access_token(identity={'username': username, 'role': user['role']})
            return jsonify(access_token=access_token)
        return jsonify({"error": "Invalid credentials"}), 401

    @app.route('/jwt-protected')
    @jwt_required()
    def jwt_protected():
        return "JWT Auth: Access Granted"

    @app.route('/admin-only')
    @jwt_required()
    def admin_only():
        claims = get_jwt_identity()
        if claims['role'] != 'admin':
            return jsonify({"error": "Admin access required"}), 403
        return "Admin Access: Granted"

    if __name__ == "__main__":
        app.run()

    user@ubuntu:~/$ flask --app task_05_basic_security.py run
    ```

## 📂 Repository

- **GitHub repository:** `holbertonschool-higher_level_programming`
- **Directory:** `restful-api`