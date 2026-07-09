# # 7. Instance variable overrides a class variable
# class BankAccount:
#     # class variable
#     bank_name="HDFC"
#
#     # instance variable
#     def __init__(self, name, account_no):
#         self.name = name
#         self.account_no = account_no
#     def bank_details(self):
#         return (f"Name      : {self.name}\n"
#                 f"Account No: {self.account_no}\n"
#                 f"Bank name : {self.bank_name}\n")
# person1=BankAccount("teja","12345")
# print("Before overriding-->")
# print(person1.bank_details())
# print("After overriding-->")
# # Override class variable with an instance variable
# person1.bank_name="ICICI"
# print(person1.bank_details())
#
#
# # 8.Create a class method to update a class variable
#
# class FoodDelivery:
#     delivery_app="swiggy"
#
#     def __init__(self, customer_name,food_item):
#         self.customer_name = customer_name
#         self.food_item = food_item
#
#     @classmethod
#     def update_delivery_app(cls,new_delivery_app):
#         cls.delivery_app=new_delivery_app
#         return f"Food ordered from {cls.delivery_app} "
#     def display_details(self):
#         return (f"Customer name : {self.customer_name}\n"
#                 f"food item     : {self.food_item}\n"
#                 f"Delivery app  : {self.delivery_app}")
#
# customer1=FoodDelivery("teja","biryani")
# print("Before updating class variable using class method-->")
# print(customer1.display_details())
# customer1.update_delivery_app("Zomato")
# print("\nAfter updating class variable using class method-->")
# print(customer1.display_details())
#
#
# # 9. static method that performs addition of two numbers
# class calculations:
#     @staticmethod
#     def add(a, b):
#         return a + b
#     def addition(self):
#         return f"addition:{self.add(4,6)}"
# obj=calculations()
# print(obj.add(8,9))
# print(obj.addition())
#
# # 10.Create a class BankAccount with methods deposit()and withdraw()

# class BankAccount:
#     bank_name="HDFC"
#     def __init__(self, name, account_no):
#         self.name = name
#         self.account_no = account_no
#         self.balance = 2_00_000
#
#     def deposit(self,amount):
#         self.balance += amount
#         return f"Balance after deposit :{self.balance}"
#
#     def withdraw(self,amount):
#         self.balance -= amount
#         return f"Balance after withdraw : {self.balance}"
#
# user1=BankAccount("Teja","12345")
# deposit_amt=float(input("Enter amount to be deposited :"))
# print(user1.deposit(deposit_amt))
# print(user1.withdraw(2000))

# 11. Create a class where one method calls another method inside the same class.

# class Calculator:
#     def __init__(self):
#         self.__balance=0
#     def add(self,num1,num2):
#         self.__balance+=(num1+num2)
#         return self.__balance
#     def sub(self,num1,num2):
#         self.__balance += (num1 - num2)
#         return self.__balance
#     def multiply(self,num1,num2):
#         self.__balance += (num1 * num2)
#         return self.__balance
#     def divide(self,num1,num2):
#         self.__balance += (num1 / num2)
#         return self.__balance
#
#     def display(self):
#         return (f"Addition       : {self.add(2,3)}\n"
#                 f"balance       :  {self.__balance}\n"
#                 f"Subtraction    : {self.sub(6,3)}\n"
#                 f"balance       :  {self.__balance}\n"
#                 f"Multiplication : {self.multiply(2,3)}\n"
#                 f"balance       :  {self.__balance}\n"
#                 f"Division       : {self.divide(9,3)}\n"
#                 f"balance       :  {self.__balance}")
#
# calc=Calculator()
# print(calc.display())


# 12.Create a class where the constructor initializes a list and perform operations on it.

# class StudentList:
#     def __init__(self,student_names):
#         self.student_names=student_names
#
#     def display(self):
#         for student in self.student_names:
#             print(student)
#
# class1=StudentList(["a","b","c"])
# class1.display()

# 13. Implement a class with a private variable and create getter and setter methods.

# class Private:
#     def __init__(self):
#         self.__private="private"
#     def display(self):
#         print(self.__private)
# class Public(Private):
#     def __init__(self):
#         super().__init__()
#     # def display(self):
#     #     print(self._Private__private)
#
# obj=Public()
# obj.display()


# class Employee:
#     def __init__(self,name,age,salary):
#         self.name = name
#         self._age = age
#         self.__salary = salary
#
#     # name getter setter deleter
#
#     @property
#     def name(self):
#         self.__name
#
#     @name.getter
#     def name(self):
#         print("from name getter")
#         return self._name
#
#     @name.setter
#     def name(self,name_val):
#         print("from name setter")
#         if not isinstance(name_val,str):
#             raise ValueError("Name must be a string")
#         self._name = name_val
#
#     @name.deleter
#     def name(self):
#         print("from name deleter")
#         del self._name
#
#     #age getter setter deleter
#
#     @property
#     def age(self):
#         self._age
#
#     @age.getter
#     def age(self):
#         print("from age getter")
#         return self._age
#
#     @age.setter
#     def age(self,age_val):
#         print("from age setter")
#         if not isinstance(age_val,int):
#             raise ValueError("Age must be a number")
#         self._age = age_val
#
#     @age.deleter
#     def age(self):
#         print("from age deleter")
#         del self._age
#
#     # sal setter getter deleter
#
#     @property
#     def salary(self):
#         self.__salary
#
#     @salary.getter
#     def salary(self):
#         print("from salary getter")
#         return self.__salary
#
#     @salary.setter
#     def salary(self,salary_val):
#         print("from salary setter")
#         if not isinstance(salary_val,int):
#             raise ValueError("Salary must be a number")
#         self.__salary = salary_val
#
#     @salary.deleter
#     def salary(self):
#         print("from salary deleter")
#         del self.__salary
#
#
# obj=Employee("Lucy","35","10000")
# # obj.age="19"
# obj.salary="10000"


# 14. Create a class with both static and class methods and demonstrate the difference.



































