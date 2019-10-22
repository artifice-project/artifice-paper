from flask import Blueprint
from flask_restful import Api
from .index import IndexResource
from .health import HealthResource
from .document import DocumentsResource

api_blueprint = Blueprint('api', __name__)
api = Api(api_blueprint)

api.add_resource(IndexResource, '/')
api.add_resource(HealthResource, '/health')
api.add_resource(DocumentsResource, '/documents/<int:document_id>', '/documents')
