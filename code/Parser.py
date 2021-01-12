from code.Quote import Quote
from code.ContentGetter import ContentGetter
from code.Author import Author


class Parser(object):
    def __init__(self, contentGetter):
        self.contentGetter = contentGetter
        self.listedAuthors = []
        self.listedTags = []

    def parse(self, bs, authors):
        quotes = []
        for div in bs.find_all(attrs={'class': 'quote'}):
            tags = []
            content = div.find('span').string
            author = div.find('small').string

            for tag in div.find_all('a'):
                if tag.has_attr('class'):
                    if("tag" in tag['class']):
                        tags.append(tag.string)
                        if(tag.string not in self.listedTags):
                            self.listedTags.append(tag.string)
                elif tag.string == "(about)" and author not in self.listedAuthors:
                    authors.append(self.parseAuthorDesc(author, tag['href']))
            quotes.append(Quote(content, author, tags))
            self.listedAuthors.append(author)
        return quotes

    def parseAuthorDesc(self, name, url):
        bs = self.contentGetter.getAuthorDesc(url)
        return Author(name,  bs.find(attrs={"class": "author-description"}).string)
