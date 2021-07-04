import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)

CURR_DIR = os.path.dirname(os.path.realpath(__file__))
print(CURR_DIR)

CURR_DIR = os.getcwd()
print(CURR_DIR)


chd = os.chdir('C:/my_project')
CURR_DIR = os.getcwd()
print(CURR_DIR)