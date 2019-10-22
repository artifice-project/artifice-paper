from flask import Blueprint

story_blueprint = Blueprint('story', __name__)

@story_blueprint.route('/')
def index():
    return '<h1>story page</h1>'
