import os
from send2trash import send2trash


def old_way(file_name):
    """ open txt file for writing
    get an error if the file name you specified exists already
    """
    do_file = open(file_name, "x")
    do_file.write("Hello, world!")
    do_file.close()


def file1(file_name):
    """ open txt file for writing
    get an error if the file name you specified exists already
    """
    with open(file_name, "x") as myfile:
        myfile.write("Hello, world!")


def read_file(file_name):
    with open(file_name, "r") as myfile:
	    print(myfile.read())
        # Return the 5 first characters of the file:
        #print(myfile.read(5))
        # Read one line of the file
        #print(myfile.readline())
        # for line in myfile:
        #     print(line)


def write_in_file(file_name, txt_content):
    """ Write to an Existing File in Python """
    with open(file_name, "a") as myfile:
	    myfile.write(txt_content)


def overwrite_file(file_name, new_content):
    """ Overwrite an Existing File in Python
    """
    with open(file_name, "w", encoding="utf8") as myfile:
	    myfile.write(new_content)
        #myfile.write("Woops! I have deleted the content!")


def old_content_in_file(file_name):
    """ Save content from file
    """
    with open(file_name, "r") as myfile:
	    old_content = myfile.read()
    return old_content


def remove_file(file_name):
    if os.path.exists(file_name):
        #os.remove(file_name)
        #os.unlink(file_name)
        send2trash(file_name)
        print(f'{file_name} was deleted')
    else:
        print(f"The file does not exist {file_name}")


def remove_dir(mydir):
    """ Under check
    """
    if os.path.exists(mydir):
        os.rmdir(mydir)
    else:
        print("The dir does not exist")


def backup(file_name):
    backups = []
    if os.path.exists(file_name):
        backups.append(old_content_in_file(file_name))
        print(f'content of {file_name} were backup')
        return backups
    else:
        print(f"The file does not exist {file_name} for backup")


# Variables
file_name = 'testfile.txt'
file_name2 = 'demofile.txt'
mydir = "300"
txt_content = "\nI'm an additional line."
new_content = 'Now the file has more content!'


# RUN FUNCTIONS
#old_way(file_name)
#file1(file_name)
#write_in_file(file_name, txt_content)
#overwrite_file(file_name, backups[0])
#read_file(file_name)
remove_file(file_name)
#remove_dir(mydir)

# for backup in backups:
#     print('backups: ', backup)
#print('\n'.join(backups))