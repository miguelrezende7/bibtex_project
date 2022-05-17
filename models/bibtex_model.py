class BibtexModel():

    def __init__(self, author, title, keywords,abstract, year, type_publication, doi,book_journal):
        self.author = author
        self.title = title
        self.keywords = keywords
        self.abstract=abstract
        self.year = year
        self.type_publication = type_publication
        self.doi = doi
        self.book_journal = book_journal

    def __repr__(self):
        return f'\n\n\nAUTHOR: {self.author}\nTITLE: {self.title}\nKEYWORDS: {self.keywords}\nABSTRACT: {self.abstract}\nYEAR: {self.year}\nTYPE PUBLICATION: {self.type_publication}\nDOI: {self.doi}\nBOOK/JOURNAL: {self.book_journal})'

    
    def dump_json(self):
        return {"Valor": {'author': self.author,
                          'title': self.title,
                          'keywords': self.keywords,
                          'abstract':self.abstract,
                          'year': self.year,
                          'type_publication': self.type_publication,
                          'doi': self.doi,
                          'book_journal': self.book_journal,

                          }}

    
    
    



    


