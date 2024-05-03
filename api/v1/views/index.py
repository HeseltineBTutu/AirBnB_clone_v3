"""
Module for defining routes for API v1 views.
"""

from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status')
def status():
    """
    Returns a JSON object with status OK.
    """
    return jsonify({"status": "OK"})
