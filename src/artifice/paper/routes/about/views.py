from flask import Blueprint

about_blueprint = Blueprint('about', __name__)

@about_blueprint.route('/')
def index():
    return '<h1>about page</h1>'
