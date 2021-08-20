import requests
from bs4 import BeautifulSoup

class RequestWrapper():
    def __init__(self):
        """
        """
        pass

    def getWebContent(self, endpoint):
        """
        """
        res = requests.get(endpoint)
        assert res.status_code == 200, "Response Code was not 200"
        return res.content

    def getSoup(self, endpoint):
        """
        """
        return BeautifulSoup(self.getWebContent(endpoint))