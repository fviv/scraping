import requests
import lxml
from bs4 import BeautifulSoup

class Parser(object):
    def __init__(self, url):
        self.url = url
    def Parse(self,pageNumber):
        return(BeautifulSoup(requests.get(self.url+str(pageNumber)).text,'lxml'))