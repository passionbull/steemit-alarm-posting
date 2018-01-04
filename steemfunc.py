from steem import Steem
import time

class Steemfunc:
    def __init__(self):
        self.steemNode = Steem()
        self.num_posts = 1
        self.sort = 'created'
        self.tag = 'kr-dev'

    def get_latest_posts(self, _sort='created', _tag='kr-dev', _period=1):
        posts = self.steemNode.get_posts(self.num_posts,_sort,_tag)
        post = posts[0]
        return post

    def print_post_link(self, _post):
        url = 'http://steemit.com/'+_post['tags'][0]+'/@'+_post['author']+'/'+_post['permlink']
        print(url)
        
    def get_post_link(self, _post):
        url = 'http://steemit.com/'+_post['tags'][0]+'/@'+_post['author']+'/'+_post['permlink']
        return url


