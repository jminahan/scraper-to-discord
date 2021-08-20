import abc

class ScraperConfig(abc.ABC):
    """
        Purpose: This class holds metadata info about a scraper config.  This helps to standaradize article sources
    """
    def __init__(self,
                    scraper_name,
                    scraper_endpoint):
        """
        """
        self.scraper_name = scraper_name
        self.scraper_endpoint = scraper_endpoint

    def getName(self):
        """
            Purpose: Scraper name should be human readable and unique
        """
        return self.scraper_name

    def getEndpoint(self):
        """
            Purpose: Endpoint should be where the program scrapes to check whether or not there are any new aritlces
        """
        return self.scraper_endpoint