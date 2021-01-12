class Quote(object):
    def __init__(self, content, author, tags):
        self.content = content
        self.author = author
        self.tags = tags

    def toMarkdownLine(self):
        i = len(self.tags)
        formattedTags = ""
        for tag in self.tags:
            formattedTags += tag
            i -= 1
            if(i != 0):
                formattedTags += ", "
        return self.content+" | "+self.author+" | "+formattedTags+"\n"
