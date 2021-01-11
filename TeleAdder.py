print ("")
print ("  ______                                    _____   ______    ______   __        ______ ")
print ("")
print ("88888888888        888          ")                                 
print ("     888             888           ")                               
print ("     888             888                ")                           
print ("     888   .d88b.     888   .d88b.     ")                              
print ("     888 d8P  Y8b   888  d8P  Y8b    ")                              
print ("     888 88888888   888  88888888    ")                              
print ("          888         888 888        ")                             
print ("            8888888  888   8888888      ")                             
print ("                                    ")                                            
print ("                                          ")                                      
print ("                                            ")                                    
print (" .d8888b.                                       ")                                
print ("d88P  Y88b                                   ")                                   
print ("Y88b.                                                 ")                          
print ("  Y888b.    .d8888b  8888b.  888d888 8888b.   88888b.  88888b.   .d88b.   888d888  ")
print ("    Y88b. d88P          88b  888P        88b  888 88b  888  88b  d8P  Y8b 888P   ")
print ("      888 888       d888888 888    .d888888  888  888 888  888 88888888  888     ")
print ("Y88b  d88P Y88b.    888  888 888   888  888 888 d88P 888 d88P Y8b.     888     ")
print (" Y8888P     Y8888P  Y888888 888    Y888888 88888P   88888P    Y8888  888     ")
print ("                                                   888      888                       ")
print ("                                                   888      888                     ")  
print ("__________________________________________")
print ("|!   Youtube Channel:- Neutral Army      |")
print ("|! Telegram Channel:- @Neutralarmy      !|")
print ("|!________________________________________ !|")
print ("")
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty, InputPeerChannel, InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError
from telethon.tl.functions.channels import InviteToChannelRequest
import sys
import csv
import traceback
import time
import random

api_id = _________   #Enter Your 7 Digit Telegram API ID.
api_hash = '_________________________'   #Enter Yor 32 Character API Hash
phone = '_______________'   #Enter Your Mobile Number With Your Country Code.
client = TelegramClient(phone, api_id, api_hash)
async def main():
    # Now you can use all client methods listed below, like for example...
    await client.send_message('me', 'Hello !!!!!')


SLEEP_TIME_1 = 100
SLEEP_TIME_2 = 100
with client:
    client.loop.run_until_complete(main())
client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('40779'))

users = []
with open(r"Tele-Scrapped.csv", encoding='UTF-8') as f:  #Enter your file name
    rows = csv.reader(f,delimiter=",",lineterminator="\n")
    next(rows, None)
    for row in rows:
        user = {}
        user['username'] = row[0]
        user['id'] = int(row[1])
        user['access_hash'] = int(row[2])
        user['name'] = row[3]
        users.append(user)

chats = []
last_date = None
chunk_size = 1000
groups = []

result = client(GetDialogsRequest(
    offset_date=last_date,
    offset_id=0,
    offset_peer=InputPeerEmpty(),
    limit=chunk_size,
    hash=0
))
chats.extend(result.chats)

for chat in chats:
    try:
        if chat.megagroup == True:
            groups.append(chat)
    except:
        continue

print('Choose a group to add members:')
i = 0
for group in groups:
    print(str(i) + '- ' + group.title)
    i += 1

print("")
g_index = input("Enter a Number of Group: ")
target_group = groups[int(g_index)]

target_group_entity = InputPeerChannel(target_group.id, target_group.access_hash)

mode = int(input("Type 1 to add members by username or 2 to add by your ID: "))

n = 0

for user in users:
    n += 1
    if n % 80 == 0:
        sleep(60)
    try:
        print("Adding {}".format(user['id']))
        if mode == 1:
            if user['username'] == "":
                continue
            user_to_add = client.get_input_entity(user['username'])
        elif mode == 2:
            user_to_add = InputPeerUser(user['id'], user['access_hash'])
        else:
            sys.exit("Neutral Error, Try Again.")
        client(InviteToChannelRequest(target_group_entity, [user_to_add]))
        print("Waiting for 30Seconds...")
        time.sleep(random.randrange(0, 5))
    except PeerFloodError:
        print("Flood Error Generated By Telegram. TeleAdder is stopping now. Please try again after some time.")
        print("Waiting {} seconds".format(SLEEP_TIME_2))
        time.sleep(SLEEP_TIME_2)
    except UserPrivacyRestrictedError:
        print("This User Settled their account as private, so we are skipping them to add in a Group!. Skipping.")
        print("Wait for 1 Seconds...")
        time.sleep(random.randrange(0, 5))
    except:
        traceback.print_exc()
        print("Unexpected Error")
        continue
