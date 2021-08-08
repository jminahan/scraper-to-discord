import abc

class ScraperConfig(abc.ABC):
    def __init__(self,
                    scraper_name,
                    scraper_endpoint):
        self.scraper_name = scraper_name
        self.scraper_endpoint = scraper_endpoint

    def getName(self):
        return self.scraper_name

    def getEndpoint(self):
        return self.scraper_endpoint