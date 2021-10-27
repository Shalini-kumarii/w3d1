class BankAccount:
    def __init__(self,name,int_rate,balance=0):
        self.name=name
        self.int_rate = int_rate
        self.balance = balance
        
    
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if(self.balance > 500):
            self.balance -=amount
        else:
            self.balance -= 5
            print("User : "+self.name+" has insufficient funds: Charging a 5$ fee")
        return self

    def display_account_info(self,accountdetails):
        self.accountname=accountdetails
        print("User: "+self.name,self.accountname+" balance is - "+str(self.balance))
        return self

    def yield_interest(self,accountdetails):
        self.accountname=accountdetails
        self.balance +=(self.balance*self.int_rate)/100
        print("User: "+self.name,self.accountname+" after interest balance is - "+str(self.balance))
        return self

class User():
    def __init__(self,name,int_rate,balance=0):     # we assign them accordingly
        self.name = BankAccount(name,int_rate,balance)
        self.account = BankAccount(name,int_rate, balance)
        self.roth= BankAccount(name,int_rate, balance)
        
    def make_deposit(self,amount):
        self.account.deposit(amount)
        return self	                 # the specific user's account increases by the amount of the value received
    def make_withdrawal(self,amount):
        self.account.withdraw(amount)
        return self
    def display_user_balance(self,normal):
        self.account.display_account_info(normal)
        return self
    def make_yield_interest(self,normal):
        self.account.yield_interest(normal)
        return self
    def make_rothdeposit(self,amount):           	# takes an argument that is the amount of the deposit
        self.roth.deposit(amount)
        return self	                               
    def make_rothwithdrawal(self,amount):
        self.roth.withdraw(amount)
        return self
    def display_rothuser_balance(self,roth):
        self.roth.display_account_info(roth)
        return self
    def make_rothyield_interest(self,roth):
        self.roth.yield_interest(roth)
        return self

account1 = User("shalini",1,0)
account2 = User("Kumari",2,0)

account1.make_deposit(100).make_deposit(100).make_deposit(200).make_withdrawal(200).display_user_balance("normal").make_yield_interest("normal")
account1.make_rothdeposit(1000).make_rothwithdrawal(200).display_rothuser_balance("roth").make_rothyield_interest("roth")
#account2.add_account()
#account2.display_user_balance(0)


account2.make_deposit(300).make_deposit(107).make_withdrawal(100).make_withdrawal(100).make_withdrawal(100).make_withdrawal(100).display_user_balance("normal").make_yield_interest("normal")
account2.make_rothdeposit(5000).make_rothwithdrawal(200).display_rothuser_balance("roth").make_rothyield_interest("roth")
