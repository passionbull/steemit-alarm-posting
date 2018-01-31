#-*- coding:utf-8 -*-
from yamlfunc import Yamlfunc
from steemfunc import Steemfunc
from telefunc import TelegramFunc
from contextlib import suppress
import time
import telegram

users = []
targetAuthor = []
target_tag = None

pre_permlink = ['','','','','','','','','','','']
def run():
    yamlServer = Yamlfunc()
    users = yamlServer.initUsers()
    targetAuthor = yamlServer.initTargetAuthors()
    target_tag = yamlServer.user_0['target_tag']

    init_count = yamlServer.init_count
    print('Telegram setting')
    myBot = TelegramFunc(telegramKey=yamlServer.telegramKey, initBB=yamlServer.init_bb8)
    print('Steen setting')
    st = Steemfunc()

    while True:
        try:
            post = st.get_latest_posts(_tag=target_tag)
            url = st.get_post_link(post)
            if post['permlink'] != pre_permlink[0]:
                text_1 = 'Hi, I got latest post on kr-event'+'\n'+url
                for user in users:
                    #myBot.sendMessage(chat_id =user, text=text_1)
                    if init_count == 1:
                        myBot.sendMessage(user, text_1)
        except Exception as e:
            print(e)
            print('I have error on last posts')
            pass

        idx = 0
        for target_user in targetAuthor:
            idx = idx +1
            target_post = st.get_latest_user_post(_user=target_user)
            target_url = st.get_latest_user_post_link(_user=target_user)
            try:
                target_post = st.get_latest_user_post(_user=target_user)
                target_url = st.get_latest_user_post_link(_user=target_user)
                if target_post['comment']['permlink'] == None:
                    continue

                if target_post['comment']['permlink'] != pre_permlink[idx]:
                    send_text = 'Hi, I got latest post on '+ target_post['comment']['author']+'\n'+target_url
                    for user in users:
                        #myBot.sendMessage(chat_id =user, text=send_text)
                        if init_count ==1:
                            myBot.sendMessage(user, send_text)
                pre_permlink[idx] = target_post['comment']['permlink']
            except Exception as e:
                print('I have error on targetAuthor')
                pass

        pre_permlink[0] = post['permlink']
        print('I am working now')
        time.sleep(yamlServer.period_sec)
        if init_count == 0:
            init_count = 1

if __name__ == '__main__':
    with suppress(KeyboardInterrupt):
        run()
