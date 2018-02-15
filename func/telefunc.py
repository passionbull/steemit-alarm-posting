#-*- coding:utf-8 -*-

import os

import telegram
from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, Filters
class TelegramFunc:


    def start(self, bot, update):
        my_text = 'Your telegram ID is ' + str(update.message.chat_id)
        print(my_text)
        bot.send_message(chat_id=update.message.chat_id, text= my_text)
        bot.send_message(chat_id=update.message.chat_id, text='Do you want to register?\nPlease enter ID\n/id @your_id\n\nPlease enter the desired tag and users.\n/tag kr-dev kr-event\n/user jacobyu morning')

    def setting_id(self, bot, update):
        bot.send_message(chat_id=update.message.chat_id, text='Registered.\nPlease enter the desired tag and users.\n/tag kr-dev kr-event\n/user jacobyu morning')
        #insert ID to DB
        print(update.message.chat_id)
        print(update.message.text)
        user_name = update.message.text.split(' ')

    def setting_tag(self, bot, update):
        print(update.message.chat_id)
        print(update.message.text)
        bot.send_message(chat_id=update.message.chat_id, text='tag is registered.\n')
    def setting_users(self, bot, update):
        print(update.message.chat_id)
        print(update.message.text)
        bot.send_message(chat_id=update.message.chat_id, text='user is registered.\n')

    def echo(self, bot, update):
        print(update.message.chat_id)
        self.sendMessage(update.message.chat_id, update.message.text)
        #bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

    def sendMessage(self, _chat_id, _text):
        self.telegramBot.sendMessage(chat_id =_chat_id, text=_text)
        if self.initBB == 1:
            os.system('python bb8/BB8worker.py')

    def __init__(self, telegramKey, initBB):
        self.telegramKey = telegramKey
        self.telegramBot = telegram.Bot(token=telegramKey)
        self.initBB = initBB

        self.updater = Updater(token=telegramKey)
        self.dispatcher = self.updater.dispatcher
        self.start_handler = CommandHandler('start', self.start)
        self.service_handler = CommandHandler('id', self.setting_id)
        self.tag_handler = CommandHandler('tag', self.setting_tag)
        self.users_handler = CommandHandler('user', self.setting_users)
        self.echo_handler = MessageHandler(Filters.text, self.echo)
        
        self.dispatcher.add_handler(self.start_handler)
        self.dispatcher.add_handler(self.service_handler)
        self.dispatcher.add_handler(self.tag_handler)
        self.dispatcher.add_handler(self.users_handler)
        self.dispatcher.add_handler(self.echo_handler)
        self.updater.start_polling()
        #self.updater.idle()




