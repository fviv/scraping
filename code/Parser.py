'''module contenant la classe Parser'''
from code.quote import Quote
from code.author import Author


class Parser:
    '''parse les objets beautifulsoup et en extrait les informations'''

    def __init__(self, content_getter):
        self.content_getter = content_getter
        self.list_auth = []
        self.listed_tags = []

    def parse(self, beautiful_soup, authors):
        '''extracts information from a quote page'''
        quotes = []
        for div in beautiful_soup.find_all(attrs={'class': 'quote'}):
            tags = []
            content = div.find('span').string
            author = div.find('small').string

            for tag in div.find_all('a'):
                if tag.has_attr('class'):
                    if "tag" in tag['class']:
                        tags.append(tag.string)
                        if tag.string not in self.listed_tags:
                            self.listed_tags.append(tag.string)
                elif tag.string == "(about)" and author not in self.list_auth:
                    authors.append(self.parse_author_desc(author, tag['href']))
            quotes.append(Quote(content, author, tags))
            self.list_auth.append(author)
        return quotes

    def parse_author_desc(self, name, url):
        '''extracts information from an author page'''
        beautiful_soup = self.content_getter.get_author_desc(url)
        return Author(name, beautiful_soup
                      .find(attrs={"class": "author-description"}).string)
