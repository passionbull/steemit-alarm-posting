import ruamel.yaml as yaml

class Yamlfunc:
	def __init__(self):
		setting_file = open("db.yaml")
		self.settings = yaml.load(setting_file,Loader=yaml.Loader)
		self.period_sec = self.settings['period_sec']
		self.telegramKey = self.settings['telegramKey']
		self.user_0 = self.settings['user_0']



