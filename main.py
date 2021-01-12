from code.ScrapingManager import ScrapingManager

sm = ScrapingManager("http://quotes.toscrape.com",
                     "C:\\Dev\\python\\scraping\\results")
sm.scrape()
