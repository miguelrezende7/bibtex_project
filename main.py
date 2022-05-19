import pandas as pd

import yaml
from repositories.SQL.db_repository_sqlite import DbRepositorySqlite
from repositories.get_from_api import GetFromApi
from services.IO_services.exportation_services import ExportationServices
from services.IO_services.importation_services import ImportationServices
from services.convertion_services import ConvertionServices
from services.data_manipulation_services.data_services import DataServices
from services.data_manipulation_services.etl_services import Etl
from services.data_manipulation_services.yaml_services import YamlServices
from services.operation_services import OperationServices


print('\n\n\n\n\n\n\n\n\n')

# IMPORTING YAML_CONFIG_FILE
yaml_file = ImportationServices.import_yaml_config()
source =yaml_file['search_options']['source']
csv_importing_path = yaml_file['exportation_folders']['simple_files']


# GETTING SOURCE FILE 
if source=='bibtex_files':
    OperationServices.import_bibtext_from_file_and_export(yaml_file)
    # GETTING FILE FROM BIBTEXT EXPORTED 
    original_df = ImportationServices.read_csv_file(f'{csv_importing_path}csv_data.csv')
else:
    # GETTING FILE FROM API 
    original_df=OperationServices.import_from_api(yaml_file)
   

# ADD RANKING (SCI AND JCS TO IMPORTED FILE) AND EXPORT
OperationServices.add_rank_to_file_filter_and_export(yaml_file,original_df)


db=DbRepositorySqlite('Database/bancodedados.db')

# IMPORT RANKED FILE 
ranking_export_path = yaml_file['exportation_folders']['ranking_files']
json_file=ImportationServices.import_json(ranking_export_path)

db.delete_table('tblFilesWithRankings')
db.create_table()
db.insert_values_list_json(json_file)
