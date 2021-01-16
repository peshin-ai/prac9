"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import shutil
import os


def version_1():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('FilesToSort')

    # ask for which version they would like to sort by

    # sorting into folder that are specifically named
    # Make a new directory
    try:
        os.mkdir('doc')
        os.mkdir('xls')
        os.mkdir('png')
        os.mkdir('txt')
        os.mkdir('docx')
        os.mkdir('xlsx')
        os.mkdir('jpg')
        os.mkdir('gif')
    except FileExistsError:
        pass

    # Loop through each file in the (current) directory
    for filename in os.listdir('.'):
        print(filename)
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        # sort the file into the correct folders

        if ".docx" in filename:
            shutil.move(filename, 'docx/' + filename)
        elif ".xlsx" in filename:
            shutil.move(filename, 'xlsx/' + filename)
        elif ".png" in filename:
            shutil.move(filename, 'png/' + filename)
        elif ".txt" in filename:
            shutil.move(filename, 'txt/' + filename)
        elif ".doc" in filename:
            shutil.move(filename, 'doc/' + filename)
        elif ".xls" in filename:
            shutil.move(filename, 'xls/' + filename)
        elif "jpg" in filename:
            shutil.move(filename, 'jpg/' + filename)
        elif ".gif" in filename:
            shutil.move(filename, 'gif/' + filename)


if __name__ == '__main__':
    version_1()
