from services.convertion_services import ConvertionServices



class ExportationServices():
    def __init__(self):
        pass

    def export_simple(bib_obj_list,exportation_type,path):
        
        if  exportation_type == 'csv':
            ConvertionServices.convert_object_to_csv_and_save(bib_obj_list, path)
            print('Successful exporting to csv\n')
        
        elif exportation_type == 'json':
            json_file=ConvertionServices.convert_object_to_json(bib_obj_list)
            ExportationServices.export_json(json_file,path)
            print('Successful exporting to json\n')
        
        elif exportation_type == 'yaml':
            dict_list = ConvertionServices.convert_object_to_dict(bib_obj_list)
            yaml_files = ConvertionServices.convert_dict_to_yaml(dict_list)
            ExportationServices.export_yaml(yaml_files,path)
            print('Successful exporting to yaml\n')   
        
        elif exportation_type == 'xml':
            dict_list = ConvertionServices.convert_object_to_dict(bib_obj_list)
            xml_file=ConvertionServices.convert_dict_xml(dict_list)
            ExportationServices.export_xml(xml_file,path)
            print('Successful exporting to xml\n')

        else:
            print('exportation type not found')
        
  
    def export_ranking(merged,exportation_type,path):
        dict_list=ConvertionServices.convert_csv_to_dict_list(merged)
        
        if  exportation_type == 'csv':
            ExportationServices.export_csv(merged,path)
            print('Successful exporting to csv\n')
            pass
        elif exportation_type == 'json':
            json_file=ConvertionServices.convert_dict_to_json(dict_list)
            ExportationServices.export_json(json_file,path)
            print('Successful exporting to json\n')        
        elif exportation_type == 'yaml':
            yaml_export_file=ConvertionServices.convert_dict_to_yaml(dict_list)
            ExportationServices.export_yaml(yaml_export_file,path)
            print('Successful exporting to yaml\n')        
        elif exportation_type == 'xml':
            xml_file=ConvertionServices.convert_dict_xml(dict_list)
            ExportationServices.export_xml(xml_file,path)
            print('Successful exporting to xml\n') 

        else:
            print('exportation type not found')
        
        
      
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
