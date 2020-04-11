import os
import platform
import time
import subprocess

host=platform.system()
nopool=False

print ('''


 _______     ____  __ _
|  __ \ \   / /  \/  (_)
| |__) \ \_/ /| \  / |_ _ __   ___ _ __
|  ___/ \   / | |\/| | | '_ \ / _ \ '__|
| |      | |  | |  | | | | | |  __/ |
|_|      |_|  |_|  |_|_|_| |_|\___|_|

Another Open-Source Project By hpott
             v0.0.1
''')
address = open("address.txt", 'r')

with open('address.txt', 'r') as address:
    line = address.readline()

    if line.strip() == "[Replace this with your mining address]":
        print ("No valid address found, please enter mining address into address.txt.")
        quit()

with open("config/pool.txt", 'r') as poolread:
    pool = poolread.readline()
    pool = pool.strip()

    if pool == ("none"):
        paddress=raw_input("No saved pool found. Please enter a pool address: ")
        poolport=raw_input("Please enter your pool's mining port: ")
        nopool=True
if nopool:
    with open("config/pool.txt", 'w') as poolwrite:
        poolwrite.write(paddress+":"+poolport+"\n")
        fullpadress=(paddress+":"+poolport)
        print fullpadress
        pool=fullpadress
print ("Detected OS as "+host)
print ("Press Ctrl+C at any time to cancel mining")
if host == "Linux":
    os.system("cd bin/xmrig5.10.0-linux")
    os.system("sh runl.sh "+pool+" "+line)
elif host == "Windows":
    os.system("cd bin/xmrig5.10.0-win")
    os.system("runw.bat "+pool+" "+line)
else:
    print ("Your OS is not currently compatible with PYMiner")
    quit()
