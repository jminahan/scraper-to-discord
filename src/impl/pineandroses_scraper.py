from custInterfaces.scraper_interface import ScraperInterface

class PineAndRosesScraper(ScraperInterface):
    def __init__(self, config):
        super().__init__(config)

    def scrape(self):
        soup = self.requestwrapper.getSoup(self.config.getEndpoint())
        return soup.find_all("h3", {"class" : "et_pb_slide_title"})

    def getMostRecent(self):
        pass

    def getNewArticles(self):
        pass