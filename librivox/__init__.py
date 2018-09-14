# librivox/__init__.py

import os
import requests

session = requests.Session()
session.params = {}

from .api import API