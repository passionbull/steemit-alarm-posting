from steem import Steem
from steemfunc import Steemfunc
from contextlib import suppress
import time
import telegram

period_sec = 1
my_token = '12345'
userId = []
userId.append('12345')
def run():
    myBot = telegram.Bot(token=my_token)
#    for user in userId:
#        myBot.sendMessage(chat_id =user, text='Hi')

    pre_permlink = ''
    st = Steemfunc()
    #post = st.get_latest_posts()
    #st. print_post_link(post)
    while True:
        post = st.get_latest_posts()
        #print(post['permlink'])
        #print(post['author'])
        url = st.get_post_link(post)
        if post['permlink'] != pre_permlink:
            text_1 = 'Hi, I got latest post on '+ post['tags'][0]
            for user in userId:
                myBot.sendMessage(chat_id =user, text=text_1)
                myBot.sendMessage(chat_id =user, text=url)
        pre_permlink = post['permlink']
        time.sleep(period_sec)

if __name__ == '__main__':
    with suppress(KeyboardInterrupt):
        run()
