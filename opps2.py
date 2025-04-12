class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no=acc
        #debit method
    def debit(self,amount):
         self.balance-=amount
         print("rs",amount,"was debited from the",self.account_no)
         print("total balance=",self.left_amount())
         #credit method
    def credit(self,amount):
        self.balance+=amount
        print("rs",amount,"was credited to your account no", self.account_no)
        print("total balance=",self.left_amount())
    def left_amount(self):
        return self.balance
        
        
acc1=Account(10000,12345)
print(acc1.balance)
acc1.debit(1000)
acc1.credit(20000)