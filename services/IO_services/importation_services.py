import json
import yaml
import pandas as pd
from models.bibtex_model import BibtexModel
from services.data_manipulation_services.bibtex_services import BibtexServices
from services.data_manipulation_services.yaml_services import YamlServices



class ImportationServices():
    def __init__(self):
        pass

    def import_yaml_config():
        with open('config.yaml', 'r') as file:
            yaml_config_file = yaml.safe_load(file)
        return yaml_config_file
    
    def import_json(path):
        with open(f'{path}json_data.json', 'r') as file:
            json_file=json.load(file)
        return json_file


    def read_csv_file(path):
        df = pd.read_csv(path,
                  sep=';', encoding='utf-8', low_memory=False,)
        return df

    def import_bibtext_files():
       
        # IMPORTING YAML CONFIG 
        yaml_file = ImportationServices.import_yaml_config()

        # Pegando caminho dos arquivos Bibtex que estão no arquivo config.yaml
        bibtex_files_path = YamlServices.get_path_from_yaml(yaml_file)
      
        # Pegando Lista de arquivos Bibtex
        file_list = BibtexServices.get_file_list(bibtex_files_path)

        # Importando Bibtex
        bib_list = BibtexServices.read_bibtex_from_folder(file_list)

        return bib_list

