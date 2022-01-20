from Domain.website import Website


class FileRepository:
    def __init__(self, file_name):
        self.__file_name = file_name
        self.__storage = []

    def read_file(self):

        try:
            with open(self.__file_name, 'r') as fp:
                for line in fp:

                    components = line.split(' ')
                    name = components[0]
                    url = components[1]
                    container_class = components[2]
                    classes = components[3::]
                    website = Website(name,url, container_class, classes)
                    self.add(website)
        except:
            self.__storage = {}

    def get_all(self):
        return self.__storage

    def add(self, website: Website):
        self.__storage.append(website)
