import sys
class Customer:
    """Customer class with bank operations"""
    bankname = 'SBI'
    
    def __init__(self,name,balance=0.0):
        self.name = name
        self.balance = balance
        
    def Deposit(self,amount):
        self.balance = self.balance + amount
        print('Balance after deposit:',self.balance)
        
    def Withdraw(self,amount):
        if amount>self.balance:
            print('Insufficient Funds in your account... cannot perform action')
            sys.exit()
        self.balance = self.balance-amount
        print('Balance after withdraw: ',self.balance)
    
print("Welcome to",Customer.bankname)
name = input('Enter your Name:')
c = Customer(name)
while True:
    print("d-Deposit\n w-Withdraw\n e-exit")
    option = input('Enter your option:')
    
    if option == 'd' or option == 'D':
        amount = float(input('Enter amount:'))
        c.Deposit(amount)
    elif option == 'w' or option == 'W':
        amount = float(input('Enter amount:'))
        c.Withdraw(amount)
    elif option == 'e' or option == 'E':
        print("Thank you for Banking")
        sys.exit()
        
    else:
        print('Invalid option... Please choose correct option')