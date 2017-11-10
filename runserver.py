"""
This script runs the python_webapp_flask application using a development server.
"""

from os import environ
import os
from python_webapp_flask import app # import app
from flask import jsonify


@app.route('/first_endpoint', methods=["GET"])
def test_function():
    print("let's get WHACK going!")
    print(os.environ["secret"])
    return jsonify(name=f"hey")

if __name__ == '__main__':
    app.run(host = "localhost", port=5555, debug=True)
