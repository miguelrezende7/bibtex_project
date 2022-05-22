import bibtexparser
from flask_restful import Api, Resource, reqparse
from flask import Flask, request
import werkzeug

from werkzeug.datastructures import FileStorage
from services.convertion_services import ConvertionServices

from services.operation_services_api import OperationServicesApi


# def normalize_path_params(source='api',
#                           search_words='BIG DATA',
#                           title='',
#                           keywords='',
#                           year_equality='',
#                           year='',
#                           type_publication='',
#                           jcr_value_equality='',
#                           jcr_value='',
#                           scimago_value_equality='',
#                           scimago_value='', **dados
#                           ):
#     return {
#         'source': source,
#         'search_words': search_words,
#         'title': title,
#         'keywords': keywords,
#         'year_equality': year_equality,
#         'year': year,
#         'type_publicati`
#         on': type_publication,
#         'jcr_value_equality': jcr_value_equality,
#         'jcr_value': jcr_value,
#         'scimago_value_equality': scimago_value_equality,
#         'scimago_value': scimago_value,
#     }


# path_params = reqparse.RequestParser()
# path_params.add_argument('source', type=str, location='args')
# path_params.add_argument('search_words', type=str, location='args')
# path_params.add_argument('title', type=str, location='args')
# path_params.add_argument('keywords', type=str, location='args')
# path_params.add_argument('year_equality', type=str, location='args')
# path_params.add_argument('year', type=str, location='args')
# path_params.add_argument('type_publication', type=str, location='args')
# path_params.add_argument('jcr_value_equality', type=str, location='args')
# path_params.add_argument('jcr_value', type=str, location='args')
# path_params.add_argument('scimago_value_equality', type=str, location='args')
# path_params.add_argument('scimago_value', type=str, location='args')


class BibtexApi(Resource):
    
    path_params = reqparse.RequestParser()
    path_params.add_argument('source',type='str',location='args')
    # path_params.add_argument('search_words')
    # path_params.add_argument('title')
    # path_params.add_argument('keywords')
    # path_params.add_argument('abstract')
    # path_params.add_argument('year_equality')
    # path_params.add_argument('year')
    # path_params.add_argument('type_publication')
    # path_params.add_argument('doi')
    # path_params.add_argument('jcr_value_equality')
    # path_params.add_argument('jcr_value')
    # path_params.add_argument('scimago_value_equality')
    # path_params.add_argument('scimago_value')




    def get(self):
        print('\n\n\n')
        path_params = reqparse.RequestParser()
        path_params.add_argument('source',type=str,default='',location='args')
        path_params.add_argument('search_words',type=str,default='',location='args')
        path_params.add_argument('title',type=str,default='',location='args')
        path_params.add_argument('keywords',type=str,default='',location='args')
        path_params.add_argument('abstract',type=str,default='',location='args')
        path_params.add_argument('year_equality',type=str,default='==',location='args')
        path_params.add_argument('year',type=str,default='',location='args')
        path_params.add_argument('type_publication',type=str,default='article',location='args')
        path_params.add_argument('doi',type=str,default='',location='args')
        path_params.add_argument('jcr_value_equality',type=str,default='',location='args')
        path_params.add_argument('jcr_value',type=str,default='',location='args')
        path_params.add_argument('scimago_value_equality',type=str,default='',location='args')
        path_params.add_argument('scimago_value',type=str,default='',location='args')
        dados=path_params.parse_args()
        
    


        if dados['source']=='api':
            
            valor=OperationServicesApi.process_api(dados)
            print('\n\n\n')

        else:
            
            
            try:
                data = request.files.get("bibtex")
                bib_database = bibtexparser.load(data)
                biblist=[bib_database] 
                bib_obj=ConvertionServices.convert_bibtex_files_list_to_object_list(biblist)
                valor=OperationServicesApi.process_api(dados,bib_obj)
            except:
                return {'bibtex': 'Error with bibtexfile'}
   
        
            
        
        return valor
    
    def post(self):
        print('\n\n\n')

        # path_params = Api.parser()
        # path_params.add_argument('bibtex_file', type=werkzeug.datastructures.FileStorage, location='form')
        # path_params.add_argument('bibtex_file2', type=werkzeug.datastructures.FileStorage, location='files')
        # path_params.add_argument('bibtex_file3', type=FileStorage, location='form')
        # path_params.add_argument('bibtex_file4', type=FileStorage, location='files')
        # dados = path_params.parse_args()
        # print(dados)
        
        data = request.files.get("bibtex")
       
        bib_database = bibtexparser.load(data)
        biblist=[bib_database]
        
        bib_obj=ConvertionServices.convert_bibtex_files_list_to_object_list(biblist)
        print(bib_obj)

        # OperationServicesApi.initial(dados)
        # # dados_validos = {chave:dados[chave] for chave in dados if dados[chave] is not None}
        # for key, value in dados.items():
        #     if (value == None):
        #         value = ''
        # print(dados)
        
        
        
        return {'bibtex': 'teste'}
