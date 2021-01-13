'''module contenant la classe Quote'''


class Quote:
    '''classe stockant les informations pour un quote
     et qui contient une méthode pour le formatter en md'''

    def __init__(self, content, author, tags):
        self.content = content
        self.author = author
        self.tags = tags

    def to_markdown_line(self):
        '''converts this quote's informations to a markdown table line'''
        i = len(self.tags)
        formatted_tags = ""
        for tag in self.tags:
            formatted_tags += tag
            i -= 1
            if i != 0:
                formatted_tags += ", "
        return self.content+" | "+self.author+" | "+formatted_tags+"\n"
