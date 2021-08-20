from src.Interfaces.scraper_interface import ScraperInterface

class PineAndRosesScraper(ScraperInterface):
    def __init__(self, config):
        """
        """
        super().__init__(config)

    def scrape(self):
        """
            Purpose : Scrape the PineAndRoses main webpage -- gets the main title
        """
        soup = self.requestwrapper.getSoup(self.config.getEndpoint())
        ret_object = {}
        head_articles = soup.find_all("h3", {"class" : "et_pb_slide_title"})
        i = 0
        for art in head_articles:
            ret_object[i] = {}
            ret_object[i]["href"] = art.find_all("a")[0].get("href")
            ret_object[i]["text"] = art.find_all("a")[0].get_text()
            i += 1

        return ret_object

    def getMostRecent(self):
        """
        """
        pass

    def getNewArticles(self):
        """
        """
        pass