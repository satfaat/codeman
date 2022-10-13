import os

"""
run: 
    powershell: python3 .\dodir.py > result.txt
"""


root = os.path.join('..', 'food')
for directory, subdir_list, file_list in os.walk(root):
    print('Directory:', directory)
    for name in subdir_list:
        print('Subdirectory:', name)
    for name in file_list:
        print('File:', name)