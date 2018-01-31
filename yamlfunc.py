import ruamel.yaml as yaml

class Yamlfunc:
	def __init__(self):
		setting_file = open("db.yaml")
		self.settings = yaml.load(setting_file,Loader=yaml.Loader)
		self.period_sec = self.settings['period_sec']
		self.telegramKey = self.settings['telegramKey']
		self.user_0 = self.settings['user_0']
		self.user_1 = self.settings['user_1']
		self.init_count = self.settings['init']
		self.init_bb8 = self.settings['init_bb8']
	
	def initUsers(self):
		users = []
		users.append(yamlServer.user_0['tele_id'])
		users.append(yamlServer.user_1['tele_id'])
		return users

	def initTargetAuthors(self):
		targetAuthor = []
		targetAuthor.append(yamlServer.user_0['targetAuthor_0'])
		targetAuthor.append(yamlServer.user_0['targetAuthor_1'])
		targetAuthor.append(yamlServer.user_0['targetAuthor_2'])
		targetAuthor.append(yamlServer.user_0['targetAuthor_3'])
		targetAuthor.append(yamlServer.user_0['targetAuthor_4'])
		return targetAuthor

		




