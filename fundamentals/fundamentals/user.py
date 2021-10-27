class User:
    bank_name = "First National Dojo"              # now our method has 2 parameters!
    def __init__(self , name):   # we assign them accordingly
        self.name = name
        self.account_balance =0
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
    	self.account_balance += amount	# the specific user's account increases by the amount of the value received
    def make_withdrawal(self, amount):
        self.account_balance -=amount
    def display_user_balance(self):
        print("User: "+self.name+"balance is - "+str(self.account_balance))
    def transfer_money_to(self,amount,transfer_to):
        self.make_withdrawal(amount)
        transfer_to.make_deposit(amount)

adrian = User("Adrian")
shalini = User("Shalini")
kumari = User("Kumari")
adrian.transfer_money_to(150,kumari)
adrian.make_deposit(100)
adrian.make_deposit(100)
adrian.make_deposit(200)
adrian.make_withdrawal(200)
adrian.display_user_balance()
shalini.make_deposit(500)
shalini.make_deposit(500)
shalini.make_withdrawal(100)
shalini.make_withdrawal(100)
shalini.display_user_balance()
kumari.make_deposit(1500)
kumari.make_withdrawal(200)
kumari.display_user_balance()