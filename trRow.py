from bs4 import BeautifulSoup

class trRow:
    """
    Represents a row in the transcript table, each row contains:
        - Time information
        - Speaker information
        - Transcript of speaker dialogue
    """
    def __init__(self,tr_in):
        self.tr = tr_in
        self.text = str(self.tr.find("p"))
        self.speaker = str(self.tr.find("strong"))
        self.time = str(self.tr.find("th"))

        #Remove tags from speaker text
        self.speaker = self.speaker.replace("<strong>","")
        self.speaker = self.speaker.replace("</strong>","")

        #Remove tags text
        self.text = self.text.replace("<br/>","")
        self.text = self.text.replace('<p class="short_transcript">','')

        #Remove tags from time text
        self.time = self.time[:self.time.find("<br")] 
        self.time = self.time.replace('<p class="short_transcript">','')
        self.time = self.time.replace("<th>",'')
        self.time = self.time.replace("\n",'')


    def getText(self):
        return self.text

    def getSpeaker(self):
        return self.speaker

    def getTime(self):
        return self.time 
