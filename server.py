"""
 This project is just a mobile demo sites for new designs based on Bootstrap
 for the Aristotle Library Apps project
"""
__author__ = "Jeremy Nelson"

import datetime
import os
from bottle import request, route, run, static_file
from bottle import jinja2_view as view
from bottle import jinja2_template as template

PROJECT_ROOT = os.path.split(os.path.abspath(__file__))[0]

@route('/assets/<type_of:path>/<filename:path>')
def send_asset(type_of,filename):
    local_path = os.path.join(PROJECT_ROOT,
                              "assets",
                              type_of,
                              filename)
    if os.path.exists(local_path):
        return static_file(filename,
			   root=os.path.join(PROJECT_ROOT,
                                             "assets",
                                             type_of))

@route("/carl")
def carl():
    return template('page.html')

@route("/carl-results")
def carl_results():
    return template('carl-results.html')

@route("/current")
def current():
    return template('current')

@route("/")
def index():
    return template('index')

run(host='0.0.0.0', port=8042)
