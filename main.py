from code.Parser import Parser

p = Parser("http://quotes.toscrape.com/")
print(p.parse("1").title)