class account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account=acc

    def debit(self,amount):
        self.balance =- amount
        print("Rs.",amount, "has debited") 
        print("total amount is",self.get_balance())     
    def credit(self,amount):
        self.balance += amount
        print("Rs.",amount ,"has credit")
        print("total amount is",self.get_balance())  

    def get_balance(self):
        return self.balance

acc1=account(1000,2000)
acc1.debit(1000)
acc1.credit(1500)
acc1.get_balance()