from flask_restful import Resource, reqparse


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


path_params = reqparse.RequestParser()
path_params.add_argument('source', type=str, location='args')
path_params.add_argument('search_words', type=str, location='args')
path_params.add_argument('title', type=str, location='args')
path_params.add_argument('keywords', type=str, location='args')
path_params.add_argument('year_equality', type=str, location='args')
path_params.add_argument('year', type=str, location='args')
path_params.add_argument('type_publication', type=str, location='args')
path_params.add_argument('jcr_value_equality', type=str, location='args')
path_params.add_argument('jcr_value', type=str, location='args')
path_params.add_argument('scimago_value_equality', type=str, location='args')
path_params.add_argument('scimago_value', type=str, location='args')


class BibtexApi(Resource):
    def get(self):
        dados = path_params.parse_args()
        # dados_validos = {chave:dados[chave] for chave in dados if dados[chave] is not None}
        for key, value in dados.items():
            if (value == None):
                value = ''
        print(dados)
        
        
        
        return {'bibtex': 'teste'}
