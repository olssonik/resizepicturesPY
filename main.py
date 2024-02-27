# imports (os to open dirs and modify files, colorama to see which lines are run by the test and which are main script)
import os
from colorama import Fore, Back, Style
from PIL import Image
# sys to create a path to directory tests where i keep my tests for code
import sys
path = os.path.abspath("tests")
sys.path.append(path)


# importing tests
from listdirtest1 import dirlisted
from selectpicturetest2 import selecttest
from resizetest3 import resizetest



# Files to be resized should be all in a directory "template"
templatedir = "template"


def main():

    

    print(
        listPicturesToResize(templatedir)
        )

    selectedPicture = selectPicture()

    resize(selectedPicture, selectedPicture)
    



def resize(picture, name):

    if resizetest(picture) == True:

        current_directory = os.getcwd()

        image_path = os.path.join(current_directory, "template", picture)
    
        image = Image.open(image_path)

        height = int(input("Height: "))
        width = int(input("Width: "))


        new_size = (height, width)

        output_directory = os.path.join(current_directory, "completed")


        resized_image = image.resize(new_size)

        output_path = os.path.join(output_directory, name)
        resized_image.save(output_path)
        print("Resized version of your file should be located in the folder called completed with the same name as an original file")
    else:
        print(resizetest(picture))
            


def selectPicture():
    while True:

        selectedPicture = 0

        selectedPicture = input("Please enter exact name of the file you would like to resize: ")

        filesInTemplates = os.listdir("template")

        result = selecttest(selectedPicture, filesInTemplates)
        if result == True:
            break
    
    return selectedPicture



def listPicturesToResize(dir):

    # read all files in the template dir
    dircontents = os.listdir(dir)

    # run a test listdirtest1
    resultoftest = dirlisted(dircontents)
    
    if resultoftest == True:
        return dircontents
    elif resultoftest == False:
        print("please restart the script and make sure tests and template directories exist")


main()