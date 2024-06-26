"""
Module for defining Blueprint for API v1 views.
"""

from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

# Wildcard import of everything in the package api.v1.views.index
from api.v1.views.index import *
