import requests
#https://raw.githubusercontent.com/BrawlyTheInventor/minecraftrpg/client/mcmultiplayer.py
import requests

x = requests.get('https://raw.githubusercontent.com/BrawlyTheInventor/minecraftrpg/client/mcmultiplayer.py')

#print(x.text)

with open('mcmultiplayer.py', 'w'):
  write(x.text)
 from mcmultiplayer import *
