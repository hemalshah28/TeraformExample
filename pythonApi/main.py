from flask import Flask, request, jsonify
import os
import json
import socket


app = Flask(__name__)
@app.route('/api', methods=['GET'])

def api():
    msg = os.getenv('PING_MSG')
    if msg:
        return f'{msg}\n',200
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname) 
    return f'Hello from {hostname} ({ip_address})\n', 200

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)