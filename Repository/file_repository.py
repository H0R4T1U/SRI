from Domain.Website import Website


class FileRepository:
    def __init__(self,file_name):
        self.__file_name= file_name
        self.__storage = []

    def __read_file(self):
        pass
        '''
        try:
            with open (self.__file_name,'r') as fp:
                self.__storage = jsonpickle.decode(fp.read())
        except :
            self.__storage={}
            '''


    def get_all(self):
        self.__read_file()
        return self.__storage


    def add(self, website: Website):


        self.__storage.append(website)
