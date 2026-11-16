"""
Design a class named SavingsAccount to represent a bank savings account. The class contains:
"""
"""
Attributes:
account_id (int): identifies the account.
balance (float): the current account balance.
previous_balance (float): the account balance at the start of the previous statement period.
annual_interest_rate (float): the current annual interest rate, stored as a percent (e.g. 4.5 means 4.5%).
"""

class SavingsAccount:
    #constructor? makes things with class
    def __init__(
                self.account_id: int, 
                balance: float, 
                previous_balance: float, 
                annual_interest_rate: float): 
                self.account_id
                self.balance
                self.previous_balance
                self.annual_interest_rate
  #setter  
def set_interest_rate(self, updated_interest_rate):
    self.annual_interest_rate = updated_interest_rate
"""
A method named set_interest_rate that changes the value of annual_interest_rate.
"""
#getter
def get_monthly_interest_rate(self):
    return self.annual_interest_rate/ 12 / 100

def get_monthly_interest(self):
    self.balence * self.get_monthly_interest_rate

def get_balance_change_percent(self):
    return ((self.balence - self.previous_balance)/ self.previous_balance/ 100)

def withdraw(self, amount: float)-> None:
    if amount > self.balance:
        print("You Are Broke")
    else:
        self.balance = self.balance - amount
def deposite (self, amount:float)-> None:
    self.balence = self.balance + amount


def CQ():
    account = SavingsAccount(1122, 20_000.0, 18_500.0, 4.5)

    account.withdraw(2_500.0)
    account.withdraw(3_000.0)

    print(f"Account Id: {account.account_id}")
    print(f"current balence: {account.balence}")
    print(f"monthly interest rate: {account.get_monthly_interest_rate() * 100}%")
    print(f"monthly interest: {account.get_monthly_interest()}")
    print(f"percentage change: {account.get_balance_change_percent()}")









if __name__ == "__main__":
    CQ()
