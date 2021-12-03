# MAIN MENU
from Service.website_service import WebsiteService
from Utilities.utilities import clear_screen


class Console:
    def __init__(self,website_service:WebsiteService):
        self.__website_service = website_service

    def run_menu(self):

        print("Welcome!\n")
        print("Enter 1 to manually add the website and class names\n")
        print("Enter 2 to automatically read them from a text file\n")
        print("Enter x to quit")
        choice = input(":")
        while True:
            if int(choice) == 1:
                self.manual_run()
            elif int(choice) == 2:
                self.auto_run()
            elif choice.lower() == "x":
                quit()
            else:
                print("INVALID ANSWER!")

    def manual_run(self):
        clear_screen()
        url = input("Enter the url of the site you want to scrap,enter x to quit:")
        if url.lower() == "x":
            quit()
        classes = input("Enter the class names you want to extract (separated by a coma):").split(",")
        print(f"you want to get {url} and extract the classes:{classes}")



        self.__website_service.add(url,classes)
        self.__website_service.scrap()

    def auto_run(self):
        pass