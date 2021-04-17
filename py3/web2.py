import webbrowser
import sys
import pyperclip


link = 'https://inventwithpython.com/'
link_2 = 'https://www.google.com/maps/place/'

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open(link_2 + address)
