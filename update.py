import requests
#https://raw.githubusercontent.com/BrawlyTheInventor/minecraftrpg/server/MinecraftServer.py
import requests

x = requests.get('https://raw.githubusercontent.com/BrawlyTheInventor/minecraftrpg/server/MinecraftServer.py')

#print(x.text)

with open('MinecraftServer.py', 'w') as app:
  app.write(x.text)
