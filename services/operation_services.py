import pandas as pd
from repositories.get_from_api import GetFromApi
from services.IO_services.exportation_services import ExportationServices
from services.IO_services.importation_services import ImportationServices
from services.convertion_services import ConvertionServices
from services.data_manipulation_services.data_services import DataServices
from services.data_manipulation_services.etl_services import Etl
from services.data_manipulation_services.yaml_services import YamlServices


class OperationServices():
    def __init__(self):
        pass
     

    def import_bibtext_from_file_and_export(yaml_file):

        exportation_type_simple = yaml_file['exportation_type']['simple']
        supported_exportation_types = yaml_file['supported_exportation_types']

        # EXPORT VALITATION TYPE (SIMPLE)
        exportation_type_simple = YamlServices.exportation_type_validation(exportation_type_simple,supported_exportation_types)

        # IMPORTING BIBTEXT_FILES
        bib_list = ImportationServices.import_bibtext_files()
        # print(bib_list)

        # CONVERTING BIBTEXT_FILES_TO_BIBTEXT_OBJECTS
        bib_obj_list=ConvertionServices.convert_bibtex_files_list_to_object_list(bib_list)
        # print(bib_obj_list)

        # EXPORT SIMPLE FILE
        exportation_folder_simple = yaml_file['exportation_folders']['simple_files']
        ExportationServices.export_simple(bib_obj_list,exportation_type_simple,exportation_folder_simple)



    def import_from_api(yaml_file):
        search_words=yaml_file['search_options']['search_words']
        url=GetFromApi.url_ieee(search_words)
        # print(url)
        json_file=GetFromApi.get_from_api(url)
        # print(json_file)
        dict_ieee_formated=GetFromApi.formated_ieee_dict_from_api(json_file)
        # print(dict_ieee_formated)
        df =pd.DataFrame(dict_ieee_formated)
        return df

    def add_rank_to_file_filter_and_export(yaml_file,original_df):
        
        # VALIDATE YAML FILTER AND EXPORTATION TYPE (RANKING)
        yaml_file = YamlServices.filter_validation(yaml_file)

        # OPEN CSV FILES
        ranking_import_path = yaml_file['importation_folders']['ranking_files']
        sci = ImportationServices.read_csv_file(f'{ranking_import_path}scimagojr 2020.csv')
        jcs = ImportationServices.read_csv_file(f'{ranking_import_path}jcs_2020.csv')


        # source =yaml_file['search_options']['source']

        # if source=='api':
            
        #     original_df=import_from_api(yaml_file)
            
        # else:
            
        #     csv_importing_path = yaml_file['exportation_folders']['simple_files']
        #     original_df = ImportationServices.read_csv_file(f'{csv_importing_path}csv_data.csv')
        

        # # SCI ETL
        sci=Etl.sci_etl(sci)
        # # print(sci)


        # # JCS ETL
        jcs=Etl.jcr_etl(jcs)
        # # print(jcs)

        # # CSV ETL
        # print(original_df)
        original_df=Etl.create_upper_title(original_df,'book_journal')
        # # print(original_df)

        # # MERGING AND ETL
        merged = Etl.merge_etl(sci,jcs,original_df)
        


        # # APPLY FILTERS
        # print(f'Shape before filtering: {merged.shape}')
        merged=DataServices.filter_values(yaml_file['filter_options'],merged)
        # print(f'Shape after filtering: {merged.shape}\n')

        # # print(merged[['Year','Keywords','JCS_FACTOR','SCI_FACTOR']])
        # # print()
        # # print(merged['SCI_FACTOR'])

        exportation_type_ranking = yaml_file['exportation_type']['ranking']
        ranking_export_path = yaml_file['exportation_folders']['ranking_files']
        ExportationServices.export_ranking(merged,exportation_type_ranking,ranking_export_path)

    def import_from_api(yaml_file):
        search_words=yaml_file['search_options']['search_words']
        url=GetFromApi.url_ieee(search_words)
        # print(url)
        json_file=GetFromApi.get_from_api(url)
        # print(json_file)
        dict_ieee_formated=GetFromApi.formated_ieee_dict_from_api(json_file)
        # print(dict_ieee_formated)
        df =pd.DataFrame(dict_ieee_formated)
        return df