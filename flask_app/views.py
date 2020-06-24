from flask_app import app
import flask
from flask import request, redirect, url_for

@app.route('/')
def index():
    return flask.render_template("index.html")
    
    
@app.route('/another_page')
def another_page():
    return flask.render_template("index.html")
