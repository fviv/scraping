from code.ContentGetter import ContentGetter
from code.Parser import parse


cg = ContentGetter("http://quotes.toscrape.com/")
bs = cg.getContent("1")
parse(bs)

