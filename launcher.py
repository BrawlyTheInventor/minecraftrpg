update = input("Update & Play (y) or Play (n)?")
if update == "y":
    import requests
    #https://raw.githubusercontent.com/BrawlyTheInventor/minecraftrpg/client/mcmultiplayer.py
    import requests

    x = requests.get('https://raw.githubusercontent.com/BrawlyTheInventor/minecraftrpg/client/mcmultiplayer.py')

    #print(x.text)

    with open('mcmultiplayer.py', 'w') as app:
      app.write(x.text)
    from mcmultiplayer import *

elif update == "n":
    from mcmultiplayer import *
