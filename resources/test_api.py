import bibtexparser
from flask_restful import Api, Resource, reqparse
from flask import Flask, request
import werkzeug

from werkzeug.datastructures import FileStorage
from services.convertion_services import ConvertionServices

from services.operation_services_api import OperationServicesApi


class TestApi(Resource):
    def get(self):
        return {'bibtex': 'teste'}
