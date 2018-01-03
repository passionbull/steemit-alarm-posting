from steem import Steem
import time

num_posts = 1
period_sec = 1
sort = 'created'
tag = 'kr-dev'

if __name__ == '__main__':
	s = Steem()

	pre_permlink = '';

	while True:
		posts = s.get_posts(num_posts,sort,tag)
		post = posts[0] #get latest post
		#print(post['permlink'])
		#print(post['author'])
		url = 'http://steemit.com/'+tag+'/@'+post['author']+'/'+post['permlink']
		if post['permlink'] != pre_permlink:
			print('I got latest post on '+ tag)
			print(url)
		pre_permlink = post['permlink']
		time.sleep(period_sec)