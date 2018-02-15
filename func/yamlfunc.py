import ruamel.yaml as yaml

class Yamlfunc:
	def __init__(self):
		setting_file = open("db.yaml")
		self.settings = yaml.load(setting_file,Loader=yaml.Loader)
		self.period_sec = self.settings['period_sec']
		self.telegramKey = self.settings['telegramKey']
		self.isFirstLoopPass = self.settings['isFirstLoopPass']
		self.init_bb8 = self.settings['init_bb8']
		user_cnt = int(self.settings['user_cnt'])
		self.userInfos = []
		for x in range(0,user_cnt):
			eval_one = 'self.userInfos.append(self.settings'+"['user_"+str(x)+"'])"
			eval(eval_one)

	def getUsers(self):
		users = []
		user_cnt = int(self.settings['user_cnt'])
		for x in range(0,user_cnt):
			users.append(self.userInfos[x]['tele_id'])
			#eval_one = 'users.append(self.user_'+str(x)+"['tele_id'])"
			#eval(eval_one)
		print(users)
		return users

	def initTargetAuthors(self):
		targetAuthor = []
		for x in range(0,self.userInfos[0]['targetAuthorCnt']):
			eval_one = 'targetAuthor.append(self.userInfos[0]'+"['targetAuthor_"+str(x)+"'])"
			eval(eval_one)
		print(targetAuthor)
		return targetAuthor

	def getTargetAuthors(self, user_id):
		targetAuthor = []
		for x in range(0,self.userInfos[user_id]['targetAuthorCnt']):
			eval_one = 'targetAuthor.append(self.userInfos[user_id]'+"['targetAuthor_"+str(x)+"'])"
			eval(eval_one)
		print(targetAuthor)
		return targetAuthor		

		




