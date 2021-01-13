"""module déclencheur du scraping"""
from code.scraping_manager import ScrapingManager

sm = ScrapingManager("http://quotes.toscrape.com",
                     "C:\\Dev\\python\\scraping\\results")
sm.scrape()
