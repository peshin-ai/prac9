"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import shutil
import os


# Sorting into folder that are generally named
def version_2():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('FilesToSort')
    # Make a new directory
    try:
        os.mkdir('Images')
        os.mkdir('Spreadsheets')
        os.mkdir('Documents')
    except FileExistsError:
        pass

    # Loop through each file in the (current) directory
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        # sorting files into specific folders
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            shutil.move(filename, 'Images/' + filename)
        elif filename.lower().endswith(('.doc', '.docx', '.txt')):
            shutil.move(filename, 'Documents/' + filename)
        elif filename.lower().endswith(('.xls', '.xlsx')):
            shutil.move(filename, 'Spreadsheets/' + filename)


if __name__ == '__main__':
    version_2()
