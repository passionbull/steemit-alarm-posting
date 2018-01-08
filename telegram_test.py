from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters
from telefunc import TelegramFunc
from yamlfunc import Yamlfunc

yamlServer = Yamlfunc()
myBot = TelegramFunc(telegramKey=yamlServer.telegramKey)
