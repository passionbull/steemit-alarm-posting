from yamlfunc import Yamlfunc
from steemfunc import Steemfunc
from telefunc import TelegramFunc
from user import User
import time
import telegram


class MonitoringSystem:
    def __init__(self):
        self.Users = []
        #Start Program
        print('Yaml setting')
        yamlServer = Yamlfunc() #read db.yaml and load UserInfos
        print('Telegram setting')
        self.myBot = TelegramFunc(telegramKey=yamlServer.telegramKey, initBB=yamlServer.init_bb8) #telegram function load
        print('Steen setting')
        self.steemFunction = Steemfunc() #steem function load
        self.setUsers(yamlServer.userInfos)
        self.isFirstLoopPass = yamlServer.isFirstLoopPass # when program start, decide that loop passes or not
        self.period_sec = yamlServer.period_sec

    def setUsers(self, _userInfos):
        for user_info in _userInfos:
            user = User(user_info)
            self.Users.append(user)
    
    def alarmOnTag(self, _user):
        try:
            post = self.steemFunction.get_latest_posts(_tag=_user.target_tag)
            url = self.steemFunction.get_post_link(post)
            if post['permlink'] != _user.pre_tag:
                text_1 = 'Hi, I got latest post on '+_user.target_tag+'\n'+url
                if self.isFirstLoopPass == 0:
                    self.myBot.sendMessage(_user.tele_id, text_1)
            _user.pre_tag = post['permlink']
        except Exception as e:
            print(e)
            print("I can't get last posts")
            pass

    def alarmOnTargetAuthors(self, user):
        try:
            idx = 0
            for targetAuthor in user.targetAuthors:
                idx = idx +1
                target_post = self.steemFunction.get_latest_user_post(_user=targetAuthor)
                target_url = self.steemFunction.get_latest_user_post_link(_user=targetAuthor)
                if target_post['comment']['permlink'] == None:
                    continue
                if target_post['comment']['permlink'] != user.pre_target[idx]:
                    text_1 = 'Hi, I got latest post on '+ target_post['comment']['author']+'\n'+target_url
                    if self.isFirstLoopPass == 0:
                        self.myBot.sendMessage(user.tele_id, text_1)
                user.pre_target[idx] = target_post['comment']['permlink']
        except Exception as e:
            print(e)
            print("I can't get last posts")
            pass