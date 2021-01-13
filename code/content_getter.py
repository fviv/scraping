'''module contenant la classe ContentGetter'''
import requests
from bs4 import BeautifulSoup


class ContentGetter:
    '''classe qui effectue les requêtes http
    et retourne un objet beautifulSoup'''

    def __init__(self, domain):
        self.domain = domain

    def get_content(self, page_nb):
        '''gets quote page content'''
        return BeautifulSoup(requests.get(self.domain+"/page/"+str(page_nb))
                             .text, 'lxml')

    def get_author_desc(self, url):
        '''gets author page content'''
        return BeautifulSoup(requests.get(self.domain + url).text, 'lxml')
