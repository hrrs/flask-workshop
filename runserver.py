"""
This script runs the python_webapp_flask application using a development server.
"""

from os import environ
import os
from python_webapp_flask import app # import app
from flask import Flask,render_template, jsonify


@app.route('/first_endpoint', methods=["GET"])
def test_function():
    print("let's get WHACK going!")
    print(os.environ["secret"])
    return jsonify(name=f"hey")

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT, debug=True)
