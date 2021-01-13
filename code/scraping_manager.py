'''module contenant la classe ScrapingManager'''
from code.content_getter import ContentGetter
from code.file_writer import FileWriter
from code.parser import Parser


class ScrapingManager:
    '''classe utilisant tous les autres modules
    pour récupérer, parser et écrire dans des fichiers les citations'''

    def __init__(self, url, resultsFolderPath):
        self.content_getter = ContentGetter(url)
        self.file_writer = FileWriter(resultsFolderPath)
        self.parser = Parser(self.content_getter)

    def scrape(self):
        '''méthode principale regroupant les autres'''
        all_quotes = []
        authors = []
        i = 1
        while i < 10:
            all_quotes.extend(self.parser.parse(
                self.content_getter.get_content(i), authors))
            i += 1
        self.file_writer.write_results(
            all_quotes, authors, self.parser.listed_tags)
