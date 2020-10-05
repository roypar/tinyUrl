from model import TinyUrl
import view


def start(dbName):
    TinyUrl(dbName)
    tiny = TinyUrl.getInstance()

    view.showWelcome()

    while True:
        view.showOptions()

        option = int(input("Enter an option: "))

        if option == 0:
            break
        elif option == 1:
            url = input("Enter URL: ")
            shortUrl = tiny.makeNewEntry(url)
            view.showNewEntry(shortUrl)
        elif option == 2:
            shortUrl = input("Enter TinyURL: ")
            url = tiny.fetchOriginal(shortUrl)
            view.showFetched(url)
        elif option == 3:
            shortUrl = input("Enter TinyURL: ")
            tiny.deleteEntry(shortUrl)
            view.showDeleteEntry(shortUrl)
        elif option == 4:
            size = int(input("Enter new DB size: "))
            tiny.setDbSize(size)
            view.showDbSizeUpdate(size)

    tiny.saveInDb()
    view.showExit()


if __name__ == "__main__":
    dbName = 'tinyDB.json'
    start(dbName)