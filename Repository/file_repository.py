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
                    url = components[0]
                    container_class = components[1]
                    classes = components[2::]
                    website = Website(url, container_class, classes)
                    self.add(website)
        except:
            self.__storage = {}

    def get_all(self):
        return self.__storage

    def add(self, website: Website):
        self.__storage.append(website)
