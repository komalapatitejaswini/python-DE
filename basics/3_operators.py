# 1.check whether a number is even or odd using modulus operator

# def even_or_odd(n):
#     if n % 2 == 0:
#         return "even"
#     else:
#         return "odd"
# num = int(input("Enter a number: "))
# res=even_or_odd(num)
# print(res)

# 2.write a program using logical operators to check:Age > 18AND salary > 20000

# age=int(input("Enter your age: "))
# salary = int(input("Enter your salary: "))
# if age>18 and salary>20000:
#     print(f"person with age {age} is getting {salary} salary, so that person is experienced")
# elif salary<20000:
#     print(f"person with age {age} is getting {salary} salary, so that person is beginner")
# else:
#     print(f"person with age {age} is getting {salary} salary, so that person is student")

# 3. Write a program to check if an element exists in a list using operators

# list=[int(x) for x in input("Enter your list:").split()]
# print(list)
# element=int(input("Enter your element to search in list:"))
# if element in list:
#     print(f"{element} is in the list")
# else:
#     print(f"{element} is not in the list")

# n=int(input("Enter the number of elements:"))
# list=[]
# for i in range(n):
#     item=int(input(f"Enter the {i+1} element:"))
#     list.append(item)
# element=int(input("Enter your element to search in list:"))
# if element in list:
#     print(f"{element} is in the list")
# else:
#     print(f"{element} is not in the list")

# 4.Write a program  that checks if a number is divisible by 4.
# n=int(input("Enter a number:"))
# if n%4==0:
#     print("The number entered is divisible by 4")
# else:
#     print("The number entered is not divisible by 4")

# 5.Write a program to demonstrate operator precedence  with and without parentheses and  compare outputs.
# print((2+3)*4)
# print(2+3*4)

# 6.
# print(10 or 0 and 5)

# 7.
# print(True + True)
# print(int(True))

# 8.Write a program using bitwise operators to swap two numbers.

# a=int(input("Enter a number:"))
# b=int(input("Enter another number:"))
# a=a^b
# b=a^b
# a=a^b
# print(f"After swapping the numbers are {a} and {b}")

# 9.Write a program to check if a number is power of 2 using bitwise operator

# 10.
# print(5&3|2)
# print(10==10.0)
# print(0.1+0.2==0.3)
# print(0.1+0.2)

# 11.Write a program that finds the second largest of three numbers using operators only(no sorting).

# x=int(input("Enter a number:"))
# y=int(input("Enter another number:"))
# z=int(input("Enter another number:"))
# if x>=y and x>=z:
#     print(f"The largest number is {x} ")
#     if y>=z:
#         print(f"The second largest number is {y} ")
#     else:
#         print(f"The second largest number is {z} ")
# elif y>=z:
#     print(f"The largest number is {y} ")
#     if x>=z:
#         print(f"The second largest number is {x} ")
#     else:
#         print(f"The second largest number is {z} ")
# else:
#     print(f"The largest number is {z} ")
#     if x>=y:
#         print(f"The second largest number is {x} ")
#     else:
#         print(f"The second largest number is {y} ")

# 12.
# result = 10 + 5 * 2 > 15 and not (4 == 2 ** 2) or 7 % 3 <= 1
# print(result)

# # 1.
# print(5 > 3 > 1)
# # 2.
# print(2 << 1 + 1)
# # 3.
# print(10 == 10.0)
# x=10
# y=10.0
# print(id(x))
# print(id(y))
# print(x is y)
# # 4.
# print(not 1 == 1)
# # 5.
# print(1 & 2 | 3)
# # 6.
# print(0 or 5 and 10)
# # 7.
# print(5 ^ 3 & 1)
# # 8.
# print(~-5)
# # 9.
# print(True + False * 10)
# # 10.
# print(3 * 1 ** 3)
# # 11.
# print([] == False, [] is False)
# # 12.
# print(10 and 20 or 30)
# # 13.
# print(0 and 20 or 30)
# # 14.
# print(1 ^ 1 ^ 1)
# # 15.
# print(5 & 3 << 1)
# # 16.
# print(True << 2)
# # 17.
# print(3 + 4 * 2 ** 2)
# # 18.
# a = 256
# b = 256
# print(a is b)
# # 19.
# print(not 0 and 2 and not 3 or 4)
# # 20.
# print(5 or 0 and 3)

