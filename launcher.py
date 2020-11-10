print("Attempting to update...")
print("If update fails, go to mcsingleplayer.py, and F5")
import requests
#https://raw.githubusercontent.com/BrawlyTheInventor/minecraftrpg/client/mcmultiplayer.py

x = requests.get('https://raw.githubusercontent.com/BrawlyTheInventor/minecraftrpg/client/mcmultiplayer.py')

with open('mcmultiplayer.py', 'w') as multiupdate:
    multiupdate.write(x.text)


xsi = requests.get('https://raw.githubusercontent.com/BrawlyTheInventor/minecraftrpg/client/mcsingleplayer.py')

with open('mcsingleplayer.py', 'w') as singleupdate:
    singleupdate.write(xsi.text)

with open('mcmultiplayer.py', 'w') as multiupdate:
    multiupdate.write(x.text)
version = input("Multiplayer (m) or Singleplayer (s)?")
if version == "m":
    from mcmultiplayer import *
elif version == "s":
    from mcsingleplayer import *
