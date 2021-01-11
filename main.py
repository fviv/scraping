from code.ContentGetter import ContentGetter

cg = ContentGetter("http://quotes.toscrape.com/")
print(cg.getContent("1").title)
