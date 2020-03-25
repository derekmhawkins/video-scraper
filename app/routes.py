from flask import current_app as app, url_for, redirect, jsonify

@app.route('/')
def index():
    return "This works"