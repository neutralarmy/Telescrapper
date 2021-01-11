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
print ("|   Youtube Channel:- Neutral Army      |")
print ("|! Telegram Channel:- @Neutralarmy    !| ")
print ("|__________________________________________")
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
import csv

api_id = _________   #Enter Your 7 Digit Telegram API ID.
api_hash = '_______________________'   #Enter Yor 32 Character API Hash.
phone = '_____________'   #Enter Your Mobile Number With Country Code.
client = TelegramClient(phone, api_id, api_hash)
async def main():
    # Now you can use all client methods listed below, like for example...
    await client.send_message('me', 'Hello !!!!')
with client:
    client.loop.run_until_complete(main())
client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter verification code: '))


chats = []
last_date = None
chunk_size = 1000
groups=[]

result = client(GetDialogsRequest(
             offset_date=last_date,
             offset_id=0,
             offset_peer=InputPeerEmpty(),
             limit=chunk_size,
             hash = 0
         ))
chats.extend(result.chats)

for chat in chats:
    try:
        if chat.megagroup== True:
            groups.append(chat)
    except:
        continue

print('Choose Any Group From Which You Want To Scrap A Members:')
i=0
for g in groups:
    print(str(i) + '- ' + g.title)
    i+=1

g_index = input("Please! Enter a Number: ")
target_group=groups[int(g_index)]

print('Scrapping Members')
all_participants = []
all_participants = client.get_participants(target_group, aggressive=True)

print('Saving In file...')
with open("Tele-Scrapped.csv","w",encoding='UTF-8') as f:#Enter your file name.
    writer = csv.writer(f,delimiter=",",lineterminator="\n")
    writer.writerow(['username','user id', 'access hash','name','group', 'group id'])
    for user in all_participants:
        if user.username:
            username= user.username
        else:
            username= ""
        if user.first_name:
            first_name= user.first_name
        else:
            first_name= ""
        if user.last_name:
            last_name= user.last_name
        else:
            last_name= ""
        name= (first_name + ' ' + last_name).strip()
        writer.writerow([username,user.id,user.access_hash,name,target_group.title, target_group.id])
print('Members scraped successfully.......')
print('Join Our Telegram Channel for More Updates @Neutralarmy')
