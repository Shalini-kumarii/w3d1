class BankAccount:
    def __init__(self,name,int_rate,balance=0):
        self.int_rate = int_rate
        self.balance = balance
        self.name = name
    
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if(self.balance > 500):
            self.balance -=amount
        else:
            self.balance -= 5
            print("User : "+self.name+" has Insufficient funds: Charging a 5$ fee")
        return self

    def display_account_info(self):
        print("User : "+self.name +" balance is - "+str(self.balance))
        return self

    def yield_interest(self):
        self.balance +=(self.balance*self.int_rate)/100
        print("User :"+self.name +" after interest balance is - "+str(self.balance))
        return self


account1 = BankAccount("shalini",1,0)
account2 = BankAccount("kumari",2,0)
account1.deposit(500).deposit(100).deposit(200).withdraw(200).display_account_info().yield_interest()
account2.deposit(300).deposit(100).withdraw(100).withdraw(100).withdraw(100).withdraw(100).display_account_info().yield_interest()
