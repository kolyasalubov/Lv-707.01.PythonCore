import os
import json

#Telegram's bot token ID
TOKEN = '***********************************************'
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

#Creates json if doesn't exist
if not os.path.isfile('data.json') :
    with open("data.json", "w", encoding='utf-8') as write_file:
        json.dump([], write_file)

LIST = json.load(open('data.json'))

def listMain(update,context):
    item = update.message.text
    item = item.lower() # we read the string as lower so we won't have to deal with upper \ lower cases, and lower cases looks better than upper.
    global LIST
    
    if item == "delete all":
        LIST = []
        update.message.reply_text('list is deleted.')
        

    elif "delete" in item:
        try:
            LIST.remove(item[7:])
        except:
            LIST.pop()
        if not LIST:
            update.message.reply_text('list is deleted.')

    elif item in LIST:
        update.message.reply_text('item already exists in list.')
        return
    else:
        LIST.append(item)


    if LIST:    
        showlist = ''. join(['{}. {} \n'.format(index, item) for index,item in enumerate(LIST, start=1)])
        update.message.reply_text(showlist)
        
    """Example output:
    1. chicken
    2. wings
    3. chicken wings
    4. tomato sauce"""
    

    #save list to file everytime we edit it
    with open('data.json', 'w',encoding='utf-8') as outfile:
        json.dump(LIST, outfile, sort_keys=True, indent=4, ensure_ascii=False)


def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text, listMain))

    # Start the Bot
    updater.start_polling()
    print('bot is up and running')
    updater.idle()

main()
