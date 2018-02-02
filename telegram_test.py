#-*- coding:utf-8 -*-

from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters
from telefunc import TelegramFunc
from yamlfunc import Yamlfunc

yamlServer = Yamlfunc()
myBot = TelegramFunc(telegramKey=yamlServer.telegramKey)
myBot.sendMessage[yamlServer.user_0[tele_id],'Hello']