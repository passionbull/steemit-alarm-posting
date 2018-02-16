#-*- coding:utf-8 -*-

import os

import telegram
from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, Filters
from func.dbfunc import DBfunc
from user import User

class TelegramFunc:
    def start(self, bot, update):
        my_text = 'Your telegram ID is ' + str(update.message.chat_id)
        print(my_text)
        bot.send_message(chat_id=update.message.chat_id, text= my_text)
        bot.send_message(chat_id=update.message.chat_id, text='Do you want to register?\nPlease enter ID\n/id @your_id\n\nPlease enter the desired tag and users.\n/tag kr-dev kr-event\n/user jacobyu morning\n/status give you your status.')

    def setting_id(self, bot, update):
        # insert ID to DB
        user_name = str(update.message.text.split(' ')[1])
        tele_id = str(update.message.chat_id)

        isSuccess = self.dbconn.set_user(tele_id, user_name)
        if isSuccess == 0:
            print('update user')
            self.dbconn.update_user(tele_id, user_name)
            bot.send_message(chat_id=update.message.chat_id, text='ID is updated.\nPlease enter the desired tag and users.\n/tag kr-dev kr-event\n/user jacobyu morning')
        elif isSuccess == 1:
            print('set user')
            bot.send_message(chat_id=update.message.chat_id, text='ID is registered.\nPlease enter the desired tag and users.\n/tag kr-dev kr-event\n/user jacobyu morning')
            pass

    def setting_tag(self, bot, update):
        tele_id = str(update.message.chat_id)
        message_list = update.message.text.split(' ')
        tags = ['NULL', 'NULL', 'NULL']
        for x in range(0,len(message_list)-1):
            tags[x] = message_list[x+1]

        #self.update_target_tags(tele_id, tags)
        self.dbconn.update_tags(tele_id, tags)
        bot.send_message(chat_id=update.message.chat_id, text='target tags are set.\n')

    def setting_users(self, bot, update):
        tele_id = str(update.message.chat_id)
        message_list = update.message.text.split(' ')
        target_users = ['NULL', 'NULL', 'NULL', 'NULL', 'NULL']
        for x in range(0,len(message_list)-1):
            target_users[x] = message_list[x+1]

        #self.update_target_users(tele_id, target_users)
        self.dbconn.update_users(tele_id, target_users)
        bot.send_message(chat_id=update.message.chat_id, text='target users are set.\n')

    def get_status(self, bot, update):
        tele_id = str(update.message.chat_id)
        status = self.dbconn.get_status()
        user_1 = User(status[0], 1)
        bot.send_message(chat_id=update.message.chat_id, text='Your ID is '+ user_1.id)
        bot.send_message(chat_id=update.message.chat_id, text='Your tag is '+ user_1.target_tag)
        bot.send_message(chat_id=update.message.chat_id, text= 'Your users are ' + ", ".join(user_1.targetAuthors))

    def update_target_users(self, tele_id, target_users):
        for user in self.users:
            if user.id == tele_id:
                print("updated users")
                user.setTargetUsers(target_users)
    
    def update_target_tags(self, tele_id, target_tag):
        for user in self.users:
            if user.id == tele_id:
                print("updated tags")
                user.setTargetTags(target_tag[0])

    def echo(self, bot, update):
        print(update.message.chat_id)
        self.sendMessage(update.message.chat_id, update.message.text)
        #bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

    def sendMessage(self, _chat_id, _text):
        self.telegramBot.sendMessage(chat_id =_chat_id, text=_text)
        if self.initBB == 1:
            os.system('python bb8/BB8worker.py')

    def __init__(self, telegramKey, initBB, dbconn, users):
        self.telegramKey = telegramKey
        self.telegramBot = telegram.Bot(token=telegramKey)
        self.initBB = initBB
        self.dbconn = dbconn
        self.users = users
        #self.dbconn.get_status()
        
        self.updater = Updater(token=telegramKey)
        self.dispatcher = self.updater.dispatcher
        self.start_handler = CommandHandler('start', self.start)
        self.service_handler = CommandHandler('id', self.setting_id)
        self.tag_handler = CommandHandler('tag', self.setting_tag)
        self.users_handler = CommandHandler('user', self.setting_users)
        self.status_handler = CommandHandler('status', self.get_status)
        self.echo_handler = MessageHandler(Filters.text, self.echo)
        
        self.dispatcher.add_handler(self.start_handler)
        self.dispatcher.add_handler(self.service_handler)
        self.dispatcher.add_handler(self.tag_handler)
        self.dispatcher.add_handler(self.users_handler)
        self.dispatcher.add_handler(self.status_handler)
        self.dispatcher.add_handler(self.echo_handler)
        self.updater.start_polling()
        #self.updater.idle()




