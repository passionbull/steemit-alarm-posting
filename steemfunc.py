from steem import Steem
import time

class Steemfunc:
    def __init__(self):
        Nodes = ['https://gtg.steem.house:8090', 'https://seed.bitcoiner.me',
        'https://steemd.minnowsupportproject.org', 
        'https://steemd.privex.io', 'https://steemd.steemit.com', 'https://rpc.steemliberator.com',
        'https://steemd.minnowsupportproject.org']
        Nodes_1=['https://steemd.minnowsupportproject.org']

#        self.steemNode = Steem(Nodes)
        self.steemNode = Steem(Nodes_1)
        self.num_posts = 1
        self.sort = 'created'
        self.tag = 'kr-event'
    def get_latest_user_post(self, _user='jacobyu', _limit=1):
        posts = self.steemNode.get_blog(_user,0,_limit)
        for post in posts:
            if _user == post['comment']['author']:
                #print(post['comment']['title'])
                return post
    
    def get_latest_user_post_link(self, _user='jacobyu', _limit=1):
        posts = self.steemNode.get_blog(_user,0,_limit)
        for post in posts:
            if _user == post['comment']['author']:
                url = 'http://steemit.com/'+post['comment']['category']+'/@'+post['comment']['author']+'/'+post['comment']['permlink']
                return url

    def get_latest_posts(self, _sort='created', _tag='kr-event', _period=1):
        posts = self.steemNode.get_posts(self.num_posts,_sort,_tag)
        post = posts[0]
        return post

    def print_post_link(self, _post):
        url = 'http://steemit.com/'+_post['tags'][0]+'/@'+_post['author']+'/'+_post['permlink']
        print(url)
        
    def get_post_link(self, _post):
        url = 'http://steemit.com/'+_post['tags'][0]+'/@'+_post['author']+'/'+_post['permlink']
        return url


