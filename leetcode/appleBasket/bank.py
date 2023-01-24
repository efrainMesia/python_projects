
class BankAccount():
    def __init__(self,amt,name) -> None:
        self.amt = amt
        self.name = name
    
    def __str__(self):
        return f"Your bank account, {self.name}, has {self.amt} dollars"

if __name__=="__main__":
    t1 = BankAccount(100,'Bob')
    print(t1)