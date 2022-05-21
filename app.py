from resources.bibtex_api import BibtexApi
from resources.bibtex_api import BibtexApi
from flask import Flask
from flask_restful import Resource,Api




app = Flask(__name__)
api = Api(app)

api.add_resource(BibtexApi, '/bibtex')


if __name__ == '__main__': 
    app.run(debug=True)



# # IMPORTING YAML_CONFIG_FILE
# yaml_file = ImportationServices.import_yaml_config()
# source =yaml_file['search_options']['source']
# csv_importing_path = yaml_file['exportation_folders']['simple_files']


# # GETTING SOURCE FILE 
# if source=='bibtex_files':
#     OperationServices.import_bibtext_from_file_and_export(yaml_file)
#     # GETTING FILE FROM BIBTEXT EXPORTED 
#     original_df = ImportationServices.read_csv_file(f'{csv_importing_path}csv_data.csv')
# else:
#     # GETTING FILE FROM API 
#     original_df=OperationServices.import_from_api(yaml_file)
   

# # ADD RANKING (SCI AND JCS TO IMPORTED FILE) AND EXPORT
# OperationServices.add_rank_to_file_filter_and_export(yaml_file,original_df)



# # IMPORT RANKED FILE 
# ranking_export_path = yaml_file['exportation_folders']['ranking_files']
# json_file=ImportationServices.import_json(ranking_export_path)

# db=DbRepositorySqlite('Database/bancodedados.db')
# db.delete_table('tblFilesWithRankings')
# db.create_table()
# db.insert_values_list_json(json_file)

