from code.ContentGetter import ContentGetter
from code.FileWriter import FileWriter
from code.Parser import parse
class ScrapingManager(object):
    def __init__(self,url,resultsFolderPath):
        self.contentGetter = ContentGetter(url)
        self.fileWriter = FileWriter(resultsFolderPath)
    def scrape(self):
        allQuotes = []
        i=1
        while i<10:
            allQuotes.extend(parse(self.contentGetter.getContent(i)))
            i+=1
        self.fileWriter.writeResults(allQuotes)