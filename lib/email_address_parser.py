import re

class EmailAddressParser:
    def __init__(self, text):
        self._text = text

    def parse(self):
        parts = re.split(r'[,\s]+', self._text)
        parts = re.findall(r'[\w\.-]+@[\w\.-]+\.\w{2,}', self._text)
        return sorted(set(parts))
    

    

    

    
