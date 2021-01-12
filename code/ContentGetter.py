import requests
import lxml
from bs4 import BeautifulSoup
from code.Parser import parse


class ContentGetter(object):
    def __init__(self, domain):
        self.domain = domain

    def getContent(self, pageNumber):
        return(BeautifulSoup(requests.get(self.domain+"/page/"+str(pageNumber)).text, 'lxml'))

    def getAuthorDesc(self, url):
        return(BeautifulSoup(requests.get(self.domain + url).text, 'lxml'))
