import os
import sys

# Ensure the app directory is on the path
BASE_DIR = os.path.dirname(__file__)
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

# Import Flask app as 'application' for Passenger
from app import app as application

# Optional: set production defaults via env (Cloudways can also set these in panel)
os.environ.setdefault('FLASK_ENV', 'production')
os.environ.setdefault('PYTHONUNBUFFERED', '1')
