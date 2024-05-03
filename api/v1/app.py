#!/usr/bin/python3
"""
Module for running Flask application.
"""
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
import os

app = Flask(__name__)
app.register_blueprint(app_views)


# Handler for 404 errors
@app.errorhandler(404)
def not_found(error):
    """
    Handle 404 errors by returning a JSON-formatted response.

    Args:
        error (Exception): The exception object representing the 404 error.

    Returns:
        tuple: A tuple containing the JSON-formatted response and the HTTP
        status code (404).
    """
    return jsonify({"error": "Not found"}), 404


@app.teardown_appcontext
def teardown_db(exception):
    """
    Closes the storage"
    """
    storage.close()


if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)
