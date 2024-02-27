from colorama import Fore, Back, Style


# color the print coming from tests
def makeGreen(text):
    return print(f"{Fore.GREEN}{text}{Fore.WHITE}")

def makeRed(text):
    return print(f"{Fore.RED}{text}{Fore.WHITE}")


def selecttest(filename, existingPictures):
    makeGreen("Running test 2")
    if filename in existingPictures:
        makeGreen("You chose a file: " + filename)
        return True
    elif filename not in existingPictures:
        makeRed(filename + " doesnt exist")
        return 0
    else:
        makeRed("test2 FAILED")
        return False