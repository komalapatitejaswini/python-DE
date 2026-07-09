# class BankAccount:
#
#     bank_name="HDFC"
#     ifsc_code="HDFC001"
#
#     def __init__(self, customer_name,account_number,balance):
#         self.name = customer_name
#         self.account_number = account_number
#         self.balance = balance
#
#     # @balance.setter
#     # def balance(self, value):
#     #     self._balance = value
#
#     def deposit(self, amount):
#         self.balance += amount
#
#     def withdraw(self, amount):
#         self.balance -= amount
#
#     def account_details(self):
#         return (f"Customer Name   : {self.name}\n"
#                 f"Bank name       : {BankAccount.bank_name}\n"
#                 f"Account number  : {self.account_number}\n"
#               # f"Balance after deposit: {self.deposit(100000)}"
#               # f"Balance after withdrawal: {self.withdraw(1000)}"
#                 f"Balance         : {self.balance}\n"
#                 f"{self.account_creation()}")
#
#     @classmethod
#     def bank_details(cls):
#         return f"Bank name : {cls.bank_name}\nIFSC code :  {cls.ifsc_code}"
#
#     @staticmethod
#     def account_creation():
#         return "Account created successfully"
#
#
# account1=BankAccount("Teja",123456,10000000)
# account2=BankAccount("ram",234567,20000000)
# print("Account1 details-->")
# account1.deposit(100000)
# account1.withdraw(1000)
# print(account1.account_details())
# print("\nAccount2 details-->")
# print(account2.account_details())
# print("\nBank details-->")
# print(BankAccount.bank_details

class Account():

    def __init__(self,account_holder):
        self.account_holder=account_holder
        self.__balance=0

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self,val_balance):
        if not isinstance(val_balance,(int,float)):
            raise TypeError("Balance must be a number.")
        if val_balance<0:
            return ValueError("Balance cannot be negative.")
        self.__balance=val_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient balance")


class SavingsAccount(Account):

    def __init__(self, account_holder, interest_rate):
        super().__init__(account_holder)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * self.interest_rate / 100

class CheckingAccount(Account):

    def __init__(self, account_holder, overdraft_limit):
        super().__init__(account_holder)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):

        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Overdraft limit exceeded.")

s1 = SavingsAccount("Tejaswini", 5)
s1.deposit(10000)
print("Balance :", s1.balance)
print("Interest :", s1.calculate_interest())
print("-------------------------")
c1 = CheckingAccount("Rahul", 5000)
c1.deposit(2000)
print("Balance :", c1.balance)
c1.withdraw(6000)
print("Balance :", c1.balance)