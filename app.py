from resources.bibtex_api import BibtexApi
from resources.bibtex_api import BibtexApi
from flask import Flask
from flask_restful import Resource,Api

from resources.test_api import TestApi

app = Flask(__name__)
api = Api(app)

api.add_resource(TestApi,'/')
api.add_resource(BibtexApi, '/bibtex')


if __name__ == '__main__': 
    app.run(debug=True)



