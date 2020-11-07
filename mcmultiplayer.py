import requests
from random import randint
from time import sleep
from pygame import mixer
mixer.init()
print("Welcome to Minecraft:")
print("=====================")
print("RPG Edition")
print("Type Q in the command prompt to quit (no, not the command prompt application)")
print("Enter item and then a number to hold that item.")
print("Items: 1=sword 2=pickaxe 3=axe 4=dirt 5=wood 6,8=empty")
print("Press W, A, S, D to move")
input("Press Enter to continue")
print("Loading...")
name = input("Enter username")
x = requests.get('http://192.168.1.87:5000/returnchat')
if x.text == "'Ike: pardon " + name + "'":
    with open("banlogs.txt", "r+") as f:
        data = f.read()
        f.seek(0)
        f.write("")
        f.truncate()
    print("You have been unbanned!")
if 'client-banned' in open('banlogs.txt').read():
    raise Exception("Minecraft failed to load. You have been banned from the client")
if name == "Ike":
    if input("Enter Password") == "IkeDaMan1234":
        print('Access Granted')
    else:
        raise Exception("Incorrect Password")
sleep(2)
hearts = "10"
hearts = int(hearts)
global holding
global slot
slot = ""
holding = "1"
while True:
    x = requests.get('http://192.168.1.87:5000/returnchat')
    if x.text == "'Ike: ban " + name + "'":
        with open("banlogs.txt", "w") as banloghandler:
            print("client-banned", file=banloghandler)
            banloghandler.close()
        raise Exception("Lang.python.InternalExceptionError: Banned by server")
        mixer.music.load("3.wav")
    print("Latest chat: " + x.text)
    if holding == "1":
        holding = "Sword"
    elif holding == "2":
        holding = "Pickaxe"
    elif holding == "3":
        holding = "Axe"
    elif holding == "4":
        holding = "Dirt"
    elif holding == "5":
        holding = "Wood"
    elif holding == "6":
        holding = "Empty"
    elif holding == "7":
        holding = "Empty"
    elif holding == "8":
        holding = "Empty"
        """
    else:
        raise ValueError("Invalid slot (io.Netty.InvalidSlotError)")
        """
    hostile = randint(0, 3)
    hearts = hearts + 1
    global block
    block = ""
    blockint = randint(0, 3)
    if blockint == 0:
        block = "Grass"
    elif blockint == 1:
        blockint = "Grass"
    elif blockint == 2:
        block = "Stone"
    elif blockint == 3:
       block = "Dirt"
    if hostile == 0:
        print("No Mobs")
        hearts = hearts + 1
        mobkillable = "There is no mob."
    elif hostile == 1:
        print("A creeper!")
        hearts = hearts - 3
        mobkillable = "Killed Creeeper"
    elif hostile == 2:
        print("a Zombie!")
        hearts = hearts -2
        mobkillable = "Killed Zombie"
    elif hostile == 3:
        print("A Skeleton!")
        hearts = hearts - 1
        mobkillable = "Killed Skeleton"
    print("Hearts:")
    print(hearts)
    print("Block")
    print(block)
    print("Holding")
    print(holding)
    command = input("Enter Command: ")
    if command == "attack":
        if holding == "Sword":
            print(mobkillable)
        else:
            print("You cannot kill a mob without a sword!")
    elif command == "item":
        slot = input("Please enter item slot")
        slot = str(slot)
        holding = slot
        print("Now Holding")
        print(holding)
    elif command == " ":
        """
        if slot == 1:
            holding = slot1
        elif slot == 2:
            holding = slot2
        elif slot == 3:
            holding = slot3
        elif slot == 4:
            holding = slot4
        elif slot == 5:
            holding = slot5
        elif slot == 6:
            hoding = slot6
        elif slot == 7:
            holding = slot7
        elif slot == 8:
            holding = slot8
        print("Picked Up")
        print(block)
        """
        print("I am sorry, but this command can not be run in Stable mode")
        sleep(0.2)
        raise SyntaxError("Java.Lang.CrashReportHandler: Minecraft has crashed. Please restart")
    #BUG! funcution hearts causes io.Netty.InvalidSlotError. i wonder why?
    elif command == "funcution hearts":
        hearts = 100
    elif command == "chat":
        message = input("Enter Message ")
        #msglen = len(message)


        dictToSend = "'" + name + ": " + message + "'"
        #sendnamelen = {'namelengt':namelen}
        res = requests.post('http://localhost:5000/chatpost', json=dictToSend)
        #print('response from server:',res.text)
        print("Message sent!")
        dictFromServer = res.json()

    else:
            print("I'm sorry, but that is not a command. If you find this as a bug, please report in bugs.txt")

