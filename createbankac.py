class BankAC:
    def __init__(self,AC_Number,intial_balance=0):
     self.AC_Number = AC_Number
     self.balance = intial_balance

    def deposit(self,amount):
       if amount > 0:
          self.balance = self.balance + amount
          print(f"₹ {amount} deposited successfully.")
       else:
          print("Deposit Amount must be positive.")
        
    def withdraw(self,amount):
       if amount > 0:
          if amount <= self.balance:
             self.balance = self.balance - amount
             print(f"₹ {amount} is withdrawn successfully.")
          else:
             print("Insufficient balance.")
       else:
          print("Withdrawn Amount must be positive.")

    def check_balance(self):
       print(f"Current Balance: ₹ {self.balance} ")

# Usage 
account = BankAC(111,4000)
account.check_balance()
account.deposit(3000) 
account.withdraw(1000)
account.check_balance()
