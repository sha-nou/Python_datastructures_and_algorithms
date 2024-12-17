# creating a bank account class

class BankAcc:
    def __init__(self,cashin,cashout,remainder):
        self.cashin= cashin
        self.cashout=cashout
        self.remainder=remainder
    def __str__(self):
        return f"Shanelle recently recieved {self.cashin} and retrieved {self.cashout} and is left with {self.remainder}"
    
newAcc = BankAcc(70000,60000,10000)
print(newAcc)