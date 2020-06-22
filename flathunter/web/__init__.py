"""Initialize website module"""
from flask import Flask
from flask.logging import create_logger

app = Flask(__name__)
log = create_logger(app)

import flathunter.web.views
import flathunter.web.stats
