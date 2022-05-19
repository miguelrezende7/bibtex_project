from services.convertion_services import ConvertionServices



class ExportationServices():
    def __init__(self):
        pass

    def export_simple(bib_obj_list,exportation_type,path):
        match exportation_type: 

            case 'csv': 
                ConvertionServices.convert_object_to_csv_and_save(bib_obj_list, path)
                print('Successful exporting to csv\n')

            case 'json':
                json_file=ConvertionServices.convert_object_to_json(bib_obj_list)
                
                ExportationServices.export_json(json_file,path)
                print('Successful exporting to json\n')
 
            case 'yaml':
                dict_list = ConvertionServices.convert_object_to_dict(bib_obj_list)
                yaml_files = ConvertionServices.convert_dict_to_yaml(dict_list)
                ExportationServices.export_yaml(yaml_files,path)
                print('Successful exporting to yaml\n')
  
            case 'xml':
                dict_list = ConvertionServices.convert_object_to_dict(bib_obj_list)
                xml_file=ConvertionServices.convert_dict_xml(dict_list)
                ExportationServices.export_xml(xml_file,path)
                print('Successful exporting to xml\n')

    
    def export_ranking(merged,exportation_type,path):
        dict_list=ConvertionServices.convert_csv_to_dict_list(merged)
        
        match exportation_type:
            case 'csv': 
                ExportationServices.export_csv(merged,path)
                print('Successful exporting to csv\n')

            case 'json':
                json_file=ConvertionServices.convert_dict_to_json(dict_list)
                ExportationServices.export_json(json_file,path)
                print('Successful exporting to json\n')
 
            case 'yaml':
                yaml_export_file=ConvertionServices.convert_dict_to_yaml(dict_list)
                ExportationServices.export_yaml(yaml_export_file,path)
                print('Successful exporting to yaml\n')
  
            case 'xml':   
                xml_file=ConvertionServices.convert_dict_xml(dict_list)
                ExportationServices.export_xml(xml_file,path)
                print('Successful exporting to xml\n') 
    
    
    def export_csv(csv_file,exportation_folder):
        csv_file.to_csv(exportation_folder+'csv_data.csv')

    def export_json(json_file,exportation_folder):
        with open(exportation_folder+'json_data.json', 'w',encoding='utf-8') as outfile:
            outfile.write(json_file)

    def export_yaml(yaml_files,exportation_folder):
        with open(exportation_folder+'yaml_data.yaml', 'w',encoding='utf-8') as outfile:
            outfile.write(yaml_files)

    def export_xml(xml_files,exportation_folder):
        with open(exportation_folder+'xml_data.xml', 'w',encoding='utf-8') as outfile:
            outfile.write(xml_files)
