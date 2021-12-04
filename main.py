from Repository.file_repository import FileRepository
from Service.website_service import WebsiteService
from UI.console import Console


def main():
    website_repository = FileRepository('scrap.txt')

    website_service = WebsiteService(website_repository)

    console = Console(website_service)

    console.run_menu()


main()
