import json, redis
class User:
    def __init__(self,username,password,age,sex):
        self.username = username
        self.password = password
        self.age = age
        self.sex = sex

    def tell(self):
    print 'userContent'

class Member(User)    
	def __init__(self,username,password,age,sex)
	self.user_id = user_id
	print self.username 

    def tell(self):
    	User.tell(self)
    	if self.user_id == 1:
    		print 'This is admin'
    	else:
    		print 'This is User'




    
        
