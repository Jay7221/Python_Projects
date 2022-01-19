#! python3
#mapIt.py - opens the copied address on clpiboard in Google Maps
import webbrowser,pyperclip
address=pyperclip.paste()
webbrowser.open('https://www.google.com/maps/places'+address)
