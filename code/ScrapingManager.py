from code.ContentGetter import ContentGetter
from code.FileWriter import FileWriter
from code.Parser import Parser


class ScrapingManager(object):
    def __init__(self, url, resultsFolderPath):
        self.contentGetter = ContentGetter(url)
        self.fileWriter = FileWriter(resultsFolderPath)
        self.parser = Parser(self.contentGetter)

    def scrape(self):
        allQuotes = []
        authors = []
        i = 1
        while i < 10:
            allQuotes.extend(self.parser.parse(
                self.contentGetter.getContent(i), authors))
            i += 1
        self.fileWriter.writeResults(
            allQuotes, authors, self.parser.listedTags)
