def showWelcome():
    print("Welcome to TinyURL service!\n")


def showOptions():
    print("Enter one of the options below")
    print("Enter 1, to create new TinyURL")
    print("Enter 2, to retrieve original URL")
    print("Enter 3, to delete a TinyURL from system")
    print("Enter 4, to reset DB Size")
    print("Enter 0, to exit\n")


def showDbSizeUpdate(size):
    print(f"DB Size has been updated to {size}\n")


def showDeleteEntry(small_url):
    print(f"{small_url} has been deleted for database\n")


def showNewEntry(small_url):
    print(f"New tinyurl {small_url} created\n")


def showFetched(url):
    print(f"original url {url} fetched\n")


def showExit():
    print("Exiting, Thank You!\n")
