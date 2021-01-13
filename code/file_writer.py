'''module contenant la classe filewriter'''
from pathlib import Path
import xlsxwriter


class FileWriter:
    '''classe qui écrit les fichiers'''

    def __init__(self, results_folder):
        self.results_folder = results_folder
        Path(results_folder+"\\quotes").mkdir(parents=True, exist_ok=True)

        Path(results_folder+"\\tags").mkdir(parents=True, exist_ok=True)

        Path(results_folder+"\\authors").mkdir(parents=True, exist_ok=True)
        self.md_results_file = open(
            results_folder+"\\quotes\\quotesTable.md", "w", encoding="utf-8")
        self.txt_tags_file = open(
            results_folder+"\\tags\\tags.txt", "w", encoding="utf-8")

    def write_results(self, quotes, authors, tags):
        '''writes results in files'''
        md_string = "| Quote | Author | Tags |\n| :---: | :---: | :---: |\n"
        for quote in quotes:
            md_string += quote.to_markdown_line()
        self.md_results_file.write(md_string)
        self.md_results_file.close()
        for author in authors:
            xlsx_file = xlsxwriter.Workbook(
                self.results_folder+"\\authors\\"+author.name+".xlsx")
            worksheet = xlsx_file.add_worksheet()
            worksheet.write('A1', author.name)
            worksheet.write('A2', author.description)
            xlsx_file.close()
        tags_string = ""
        for tag in tags:
            tags_string += tag+"\n"
        self.txt_tags_file.write(tags_string)
