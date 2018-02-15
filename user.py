class User:
    def __init__(self, _user_info, num = 0):

        if num == 0:
            self.id = _user_info['id']
            self.tele_id = _user_info['tele_id']
            self.target_tag = _user_info['target_tag']
            self.targetAuthorCnt = _user_info['targetAuthorCnt']
            self.targetAuthors = []
            self.pre_tag = None
            self.pre_target = ['','','','','','','','','','','']

            for x in range(0,self.targetAuthorCnt):
                eval_one = 'self.targetAuthors.append(_user_info'+"['targetAuthor_"+str(x)+"'])"
                eval(eval_one)
            print('My ID is '+ self.id)
            print('My tag is '+ self.target_tag)
            print('My target Authors are below')
            print(self.targetAuthors)
            print('')
        if num == 1:
            self.id = _user_info[1]
            self.tele_id = _user_info[0]
            self.target_tag = _user_info[2]
            self.targetAuthorCnt = 0
            for x in range(0,5):
                if _user_info[5+x] != 'NULL':
                    self.targetAuthorCnt = self.targetAuthorCnt +1
            self.targetAuthors = []
            self.pre_tag = None
            self.pre_target = ['','','','','','','','','','','']
            for x in range(0,self.targetAuthorCnt):
                self.targetAuthors.append(_user_info[5+x])
            print('ID is '+ self.id)
            print('tag is '+ self.target_tag)
            print('target Authors are below')
            print(self.targetAuthors)
            print('')

    def setData(self, _user_info):
            self.id = _user_info[1]
            self.tele_id = _user_info[0]
            self.target_tag = _user_info[2]
            self.targetAuthorCnt = 0
            for x in range(0,5):
                if _user_info[5+x] != 'NULL':
                    self.targetAuthorCnt = self.targetAuthorCnt +1
            self.targetAuthors = []
            #self.pre_tag = None
            #self.pre_target = ['','','','','','','','','','','']
            for x in range(0,self.targetAuthorCnt):
                self.targetAuthors.append(_user_info[5+x])
            print('ID is '+ self.id)
            print('tag is '+ self.target_tag)
            print('target Authors are below')
            print(self.targetAuthors)
            print('')


    # def __init__(self, _user_db, nn):
        # self.id = _user_db[1]
        # self.tele_id = _user_db[0]
        # self.target_tag = _user_db[2]
        # self.targetAuthorCnt = 0
        # for x in range(0,5):
        #     if _user_db[5+x] != 'NULL':
        #         self.targetAuthorCnt = self.targetAuthorCnt +1
        # self.targetAuthors = []
        # self.pre_tag = None
        # self.pre_target = ['','','','','','','','','','','']
        # for x in range(0,self.targetAuthorCnt):
        #     self.targetAuthors.append(_user_db[5+x])
        # print('My ID is '+ self.id)
        # print('My tag is '+ self.target_tag)
        # print('My target Authors are below')
        # print(self.targetAuthors)
        # print('')

