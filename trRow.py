from bs4 import BeautifulSoup

class trRow:

    def __init__(self,tr_in):
        self.tr = tr_in


    def getText(self):
        return str(self.tr.find("p"))


    def getSpeaker(self):
        return str(self.tr.find("strong"))


    def getTime(self):
        return