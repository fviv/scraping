from code.Quote import Quote
def parse(bs):
    quotes = []
    for div in bs.find_all('div'):
        if('quote' in div['class']):
            tags = []
            content = div.find('span').string
            author = div.find('small').string
            for tag in div.find_all('a'):
                if tag.has_attr('class'):
                    if("tag" in tag['class']):
                        tags.append(tag.string)
            quotes.append(Quote(content,author,tags))
    return quotes

        