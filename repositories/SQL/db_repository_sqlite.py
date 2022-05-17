
import sqlite3
from repositories.SQL.db_repository_sql import DbRepository



class DbRepositorySqlite(DbRepository):
    def __init__(self,arquivo):
        self.conn=sqlite3.connect(arquivo)
        self.cursor = self.conn.cursor()

    
    def create_table(self):
        self.cursor.execute('CREATE TABLE IF NOT EXISTS "tblFilesWithRankings" ('
	                        'doi TEXT,'
	                        'author TEXT,'
	                        'title TEXT,'
                            'keywords TEXT,'
                            'abstract TEXT,'
                            'year INTEGER,'
                            'typePublication TEXT,'
                            'bookTitleJournal TEXT,'
                            'titleSCI TEXT,'
                            'sciFactor REAL,'
                            'jcsTitle TEXT,'
                            'jcsFactor REAL,'
	                        'PRIMARY KEY("doi")'
                            ')')
        self.conn.commit()
        
      
    
    def insert_values_list_json(self,data):

        # print(data)

                
        for valor in data:
            consulta = 'INSERT INTO tblFilesWithRankings (doi,author,title,keywords,abstract,year,typePublication,bookTitleJournal,titleSCI,sciFactor,jcsTitle,jcsFactor) VALUES (:doi, :author,:title,:keywords,:abstract,:year,:type_publication,:book_journal,:Title_SCI,:SCI_FACTOR ,:Title_JCS,:JCS_FACTOR)'
            self.cursor.execute(consulta,valor)
            


        self.conn.commit()
    
    def update_value_by_id(self):
        pass
    
    def delete_value_by_id(self):
        pass
    
    def delete_table(self,table_name):
        self.cursor.execute(f'DROP TABLE {table_name}')         
        self.conn.commit()
    
    def list_values_from_table(self,table_name):
        pass
    
    def close(self):
        self.cursor.close()
        self.conn.close()
        
     