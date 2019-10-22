from flask import Blueprint

basic_blueprint = Blueprint('basic', __name__)

@basic_blueprint.route('/')
def index():
    return '<h1>artifice paper homepage</h1>'
