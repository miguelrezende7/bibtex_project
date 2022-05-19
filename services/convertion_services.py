import csv
import json
import yaml
from dict2xml import dict2xml

from models.bibtex_model import BibtexModel


class ConvertionServices():

    def __init__(self):
        pass

    def convert_object_to_csv_and_save(obj_list, exportation_folder):
        filename = exportation_folder+'csv_data.csv'
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow(['author', 'title', 'keywords', 'abstract',
                            'year', 'type_publication', 'doi', 'book_journal'])

            for item in obj_list:
                writer.writerow([item.author, item.title, item.keywords, item.abstract,
                                item.year, item.type_publication, item.doi, item.book_journal])
        pass



    def convert_object_to_dict(obj_list):
        # print(list(filter(lambda x:'Maria' in x.author, obj_list)))
        dict_list=[]
        for valor in obj_list:
            dict_list.append({'author':valor.author,'title':valor.title,'keywords':valor.keywords,'abstract':valor.abstract,'year':valor.year,'type_publication':valor.type_publication,'doi':valor.doi,'book_title':valor.book_journal})
        
        
        return dict_list
    
    def convert_object_to_json(obj_list):
        json_obj = json.dumps([o.dump_json() for o in obj_list], indent=3)
        # print(json_obj)
        return json_obj

    def convert_csv_to_dict_list(csv):
        dict_file = csv.to_dict(orient='records')
        return dict_file

    def convert_dict_to_json(dict):
        json_file = json.dumps(dict,indent=3)
        return json_file

    def convert_dict_to_yaml(dict):
        yaml_file = yaml.dump(dict)
        return yaml_file

    def convert_dict_xml(dict):
        xml_file = dict2xml(dict)
        return xml_file

    def convert_bibtex_files_list_to_object_list(bib_list):
        obj_list = []
        for valor in bib_list:
            for valor2 in valor.entries:
                obj_list.append(BibtexModel(valor2.get('author', 'empty'), valor2.get('title', 'empty'), valor2.get('keywords', 'empty'), valor2.get('abstract', 'empty'), valor2.get(
                    'year', 'empty'), valor2.get('ENTRYTYPE', 'empty'), valor2.get('doi', 'empty'), valor2.get('booktitle', valor2.get('journal', 'empty'))))
        return obj_list
