

class Website:
    def __init__(self, name,url, container_class, classes):
        self.__name = name
        self.__url = url
        self.__container_class = container_class
        self.__classes = classes

    @property
    def  name(self):
        return  self.__name

    @name.setter
    def name(self,new_name):
        self.__name = new_name

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, new_url):
        self.__url = new_url

    @property
    def container_class(self):
        return self.__container_class

    @container_class.setter
    def container_class(self, new_container_class):
        self.__container_class = new_container_class

    @property
    def classes(self):
        return self.__classes

    @classes.setter
    def classes(self, new_classes):
        self.__classes = new_classes
