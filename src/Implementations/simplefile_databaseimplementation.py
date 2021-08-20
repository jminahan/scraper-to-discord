from src.Interfaces.database_interface import DatabaseInterface
from src.Models.BSM.article import Article
import json
from src.Interfaces.scaperconfig_interface import ScraperConfig

class SimpleFileDatabase(DatabaseInterface):

    def __init__(self, path_to_file_db : str):
        """
        """
        self.path_to_file_db = path_to_file_db

    def getLastArticle(self, config : ScraperConfig) -> Article:
        """
        """
        a = Article()
        jsonA = loadJson(self.path_to_file_db)[config.getName()]
        a.fromJson(jsonA)
        return a

    def putArticle(self, config: ScraperConfig, article : Article):
        """
        """
        existingData = self.loadJson(self.path_to_file_db)
        if  config.getName in [existingData.keys()]:
             if "article" in [existingData[config.getName()].keys()]:
                 existingData[config.getName()]["articles"].append(article.toJson())
             else:
                existingData[config.getName()]["articles"] = [article.toJson()]
        else:
            existingData[config.getName()] = {"articles": [article.toJson()]}
            
        self.writeJson(self.path_to_file_db, existingData)

    def writeJson(self, path, newData):
        with open(path, "w") as f:
            f.write(json.dumps(newData))
        f.close()

    def loadJson(self, path):
        with open(path, "r") as f:
            data = json.load(f)
        f.close()
        return data