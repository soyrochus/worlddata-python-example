import json

class FaoData:
    
    def __init__(self, path, db):

        self.products = []
        #self.items = []        
        with open(path, "r") as read_file:
            self.items = json.load(read_file)
            
    def get_fao_items(self):
        return self.items

class Fao:
    pass     