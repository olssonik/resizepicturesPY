from colorama import Fore, Back, Style


# color the print coming from tests
def makeGreen(text):
    return print(f"{Fore.GREEN}{text}{Fore.WHITE}")

def makeRed(text):
    return print(f"{Fore.RED}{text}{Fore.WHITE}")
    

def dirlisted(allfiles):
 
    makeRed("Running test 1")

    if len(allfiles) > 0:

        makeGreen("The list is not empty.")

        return True
    
    elif len(allfiles) < 0:

        makeRed("The list is empty.")

        return True
    
    else:

        makeRed("test failed")

        return False
    

    print("test complete")



