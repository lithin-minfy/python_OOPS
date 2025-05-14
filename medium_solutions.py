# medium 1
class vehicle:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

class car(vehicle):
    def __init__(self,make,model,year,no_of_doors,fuel_type):
        super().__init__(make,model,year)
        self.no_of_doors = no_of_doors
        self.fuel_type = fuel_type

Car = car("Toyota", "Corolla", 2020, 4, "Gasoline")
print(Car.make)  
print(Car.no_of_doors)  

# Medium 2

class BankAccount:
    def __init__(self,account_num,balance=0):
        self._account_num = account_num
        self._balance = balance

    def deposit(self,amount):
        if amount>0:
            self._balance+= amount
            return f"Deposited: {amount}, New balance: {self._balance}"
        else:
            return "amount must be in positive"
    
    def withdrawal(self,amount):
        if amount<self._balance:
            self._balance-=amount
            return f"Withdrew: {amount}, New balance: {self._balance}"
        else:
            return "Insufficient Balance"
    
    def get_balance(self):
        return self._balance

    def get_account_num(self):
        return self._account_num


account = BankAccount("123",1000)
print(account.get_balance())            
print(account.deposit(500))             
print(account.get_balance())            
print(account.withdrawal(200))           
print(account.get_balance())          
print(account.get_account_num())     

try:
    account.__balance = 9999  
    print(account.get_balance())  
except AttributeError:
    print("Cannot directly access private attribute")
