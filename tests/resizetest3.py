from colorama import Fore, Back, Style


# color the print coming from tests
def makeGreen(text):
    return print(f"{Fore.GREEN}{text}{Fore.WHITE}")

def makeRed(text):
    return print(f"{Fore.RED}{text}{Fore.WHITE}")
    

def resizetest(picture):
    makeGreen("Running test 3")

    if picture:
        return True
    else:
        makeRed("Picture doesnt exist")
        return False