import requests
import lxml
from bs4 import BeautifulSoup


class ContentGetter(object):
    def __init__(self, url):
        self.url = url

    def getContent(self, pageNumber):
        return(BeautifulSoup(requests.get(self.url+"page/"+str(pageNumber)).text, 'lxml'))
