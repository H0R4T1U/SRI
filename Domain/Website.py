

class Website:
    def __init__(self,url,classes):
        self.__url = url
        self.__classes = classes

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, new_url):
        self.__url = new_url

    @property
    def classes(self):
        return self.__classes

    @classes.setter
    def classes(self, new_classes):
        self.__classes = new_classes