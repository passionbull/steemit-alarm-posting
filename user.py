

class User:
    def __init__(self, _user_info):
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
        print('My id is '+ self.id)
        print('My target Authors are below')
        print(self.targetAuthors)
        print('')

