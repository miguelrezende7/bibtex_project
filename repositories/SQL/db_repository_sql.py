from abc import ABC,abstractclassmethod


# usar injecao de dependencia 

class DbRepository(ABC):
    def __init__(self):
        pass  
        
    @abstractclassmethod
    def insert_values_list_json(self,data):
        pass
        
    @abstractclassmethod
    def update_value_by_id(self,id):
        pass
    
    @abstractclassmethod
    def delete_value_by_id(self,id):
        pass
    
    @abstractclassmethod
    def delete_table(self,table_name):
        pass
    
    @abstractclassmethod
    def list_values_from_table(self,table_name):
        pass
        
     