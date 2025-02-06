"""
class account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no      #this attribute are public
        self.__acc_pass=acc_pass       # (  __  ) this sign can represent as a private key


    def reset_pass(self):
        print(self.__acc_pass)
     

acc1=account("25488100018456","qwertyuiop")
"""


class person:
    def __init__(self):
        __name="anonyms"
    
    def __hello(self):
        print("hello person")

    def welcome(self):
        self.__hello()

p1=person()

print(p1.welcome())