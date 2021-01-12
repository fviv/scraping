from code.Quote import Quote
from pathlib import Path


class FileWriter(object):
    def __init__(self, resultsFolder):

        Path(resultsFolder+"\\quotes").mkdir(parents=True, exist_ok=True)

        Path(resultsFolder+"\\tags").mkdir(parents=True, exist_ok=True)

        Path(resultsFolder+"\\authors").mkdir(parents=True, exist_ok=True)
        self.mdResultsFile = open(
            resultsFolder+"\\quotes\\quotesTable.md", "w", encoding="utf-8")
        self.txtTagsFile = open(
            resultsFolder+"\\tags\\tags.txt", "w", encoding="utf-8")
        self.excelAuthorsFile = open(
            resultsFolder+"\\authors\\authors.xlsx", "w", encoding="utf-8")

    def writeResults(self, quotes):
        mdString = "| Quote | Author | Tags |\n| :---: | :---: | :---: |\n"
        for quote in quotes:
            mdString += quote.toMarkdownLine()
        self.mdResultsFile.write(mdString)
        self.mdResultsFile.close()
