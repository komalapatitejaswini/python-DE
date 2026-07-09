# x=10
# def func1():
#     def func2():
#         return x
#     return func2
# y=func1()()
# print(y)

# def some(name,age):
#     if age>20:
#         return name,age
#     return name
#
# a,b=some("teja",10)
# print(a,b)

# 19.function to check whether a number is prime or not

# def is_prime(n):
#     if n==1:
#         return "Neither prime nor composite"
#     elif n>=2:
#         for i in range(2,(n//2)+1):
#             if n%i==0:
#                 return "Not Prime"
#         else:
#             return "Prime"
#     else:
#         return "Enter positive integer"
# n=int(input("Enter a number: "))
# print(is_prime(n))

# 20.calculate the area of a circle using a function

# import math
# def circle_area(radius):
#     area = math.pi * radius ** 2
#     return area
# r=int(input("Enter radius: "))
# print(circle_area(r))

# 21.accepts a list and returns the sum of all elements

# def list_sum(lst):
#     sum=0
#     for ele in lst:
#         sum+=ele
#     return sum
# lst=[1,2,3,4,5,6]
# print(list_sum(lst))

# 22. find the GCD of two numbers

# def gcd(num1, num2):
#     for i in range(min(num1, num2),0,-1):
#         if num1 % i == 0 and num2 % i == 0:
#             return i
# print(gcd(6,15))
# print(gcd(6,11))

# 23.check whether a string is a palindrome

# def palindrome(string):
#     return string == string[::-1]
# string=input("Enter a string: ")
# print(palindrome(string))

# 24. first n terms of the Fibonacci series

# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-2)+fibonacci(n-1)
# num=int(input("Enter a number of terms: "))
# for i in range(num):
#     print(fibonacci(i), end=" ")
# n=int(input("Enter a term: "))
# print(fibonacci(n-1))

# 25.*args to accept multiple numbers and return their average

def average(*nums):
    sum = 0
    for n in nums:
        sum += n
    avg = sum / len(nums)
    return sum,avg
print(average(1,2,3,4,5))

# 26.**kwargs to display student details

# def student_details(**details):
#     return details
# print(student_details(Name="Teja",Age=20))
# print(student_details(Name="Sai",Age=22,Sal=200000))
# print(student_details(Name="Harsha",Age=20,Sal=300000,Gender="Female"))

























