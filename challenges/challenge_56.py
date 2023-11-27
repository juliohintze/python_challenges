# Create a BankAccount class. It should have a account number and balance.
# It should also be possible to deposit and withdraw money from it.
# Every time the user deposits money, the balance increases.
# Every time the user withdraws money, the balance decreases.
# Then create an object from that class. Deposit some money to it and
# then print its balance.

class Bank_Account:
    def __init__(self, balance, ID):
        self.balance = balance
        self.ID = ID

# "balance" is the place where the data where money is stored, and where the "user" can withdraw their "money" from
# A function where the user adds money to their balance; this value starts from 0 (though of course, later, it will be a higher number). A person can always deposit
    def deposit(self, money):
         print(money)
         self.balance = self.balance + money
         return self.balance
       
# function where, as long as their balance is greater than 0, they can take out their money (which basically means, the money is subtracted from their balance)
    def withdraw(self, money):
        if money > 0:
            print(money)
            self.balance = self.balance - money
            return self.balance
        else:
            print("You have no money :(")

account1 = Bank_Account(1, 123456)


print(account1.deposit(27))
print(account1.withdraw(28))
print(account1.withdraw(28))