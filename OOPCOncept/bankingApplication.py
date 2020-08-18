import sys

class BankApp:
    '''Banking Application for Customer'''
    BANKNAME='AMJAD-BANK PVT LTD.'

    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance
    
    def deposite(self,amt):
        self.balance=self.balance+amt
        print("Amount Deposited in your saving Account" ,self.balance)
    
    def withdraw(self,amt):
        if amt>self.balance:
            print("Insufficent Balance for Transaction.. Please Contact nearest branch")
            sys.exit()
        self.balance=self.balance-amt
        print("Current Balance ",self.balance)
    
print("Welcome to ", BankApp.BANKNAME)
name=input("Please Enter your Name : ")
c=BankApp(name)
while True:
    print("chose from below option \nd-Deposite \nw-Withdraw \ne-Exit")
    option=input("Enter Your Option:")
    if option=='d' or option=='D':
        amt=float(input("Enter Amount :"))
        c.deposite(amt)
    elif option=='w' or option=="W":
        amt=float(input("Enter Amount :"))
        c.withdraw(amt)
    elif option=='e' or option=='E':
        print("Thanks for Banking with",BankApp.BANKNAME,"We Look Ahead for more Transaction")
        sys.exit()
    else:
        print("You have to Enter Option from here")

        
    