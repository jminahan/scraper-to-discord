import abc

class messageInt(abc.ABC):

    def __init__(self):
        pass

    @abc.abstractclassmethod
    def printMessage(self):
        """
        Hello World
        """
        pass