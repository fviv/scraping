from code.Quote import Quote
from pathlib import Path
import xlsxwriter


class FileWriter(object):
    def __init__(self, resultsFolder):
        self.resultsFolder = resultsFolder
        Path(resultsFolder+"\\quotes").mkdir(parents=True, exist_ok=True)

        Path(resultsFolder+"\\tags").mkdir(parents=True, exist_ok=True)

        Path(resultsFolder+"\\authors").mkdir(parents=True, exist_ok=True)
        self.mdResultsFile = open(
            resultsFolder+"\\quotes\\quotesTable.md", "w", encoding="utf-8")
        self.txtTagsFile = open(
            resultsFolder+"\\tags\\tags.txt", "w", encoding="utf-8")

    def writeResults(self, quotes, authors, tags):
        mdString = "| Quote | Author | Tags |\n| :---: | :---: | :---: |\n"
        for quote in quotes:
            mdString += quote.toMarkdownLine()
        self.mdResultsFile.write(mdString)
        self.mdResultsFile.close()
        for author in authors:
            print(author.description)
            xlsxFile = xlsxwriter.Workbook(
                self.resultsFolder+"\\authors\\"+author.name+".xlsx")
            worksheet = xlsxFile.add_worksheet()
            worksheet.write('A1', author.name)
            worksheet.write('A2', author.description)
            xlsxFile.close()
