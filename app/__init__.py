#!/usr/bin/env python3
#
# this is a major re-write/refactor of my dice2.py script. this update will provide a web UI thanks to Flask. The dice
# logic will be converted into a class, and the web UI will be crafted to be flexible and easy to expand for other
# RPG gaming needs/wants

# let's get to importing
from flask import Flask


# we're naming the app web_dice
app = Flask(__name__)

from app import routes
