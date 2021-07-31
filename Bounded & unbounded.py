# Unbounded Method

class Bank:
    def Holder(ip,pwd):
        print(ip,pwd)
    def Login(ip):
        print(ip)
Bank.Holder('3.3.3.3','147')
Bank.Login('3.3.3.3')


# Bounded Method


class Bank:
    def __init__(self,ip,pwd):
        self.ip = ip
        self.pwd = pwd
    def Holder(self):
        print(self.ip,self.pwd)
    def Login(self):
        print(self.ip)
        
My = Bank('3.3.3.3','147')
My.Holder()
My.Login()

