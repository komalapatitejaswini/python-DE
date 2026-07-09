# # 1. Write a program to print your name, course, and city.
# name=input("Enter your name:")
# course=input("Enter your course:")
# city=input("Enter your city:")
# print(name)
# print(course)
# print(city)
#
# # single line comments
# # 2. Write a program showing the use of comments.
# """
# multi line comment
# line1
# line2
# line3
# """
# '''
# another way of multi line comment
# lin1
# lin2
# lin3
# '''
#
# # 3. Write a program to print formatted output using multiple print statements.
#
# name=input("Enter your name:")
# course=input("Enter your course:")
# city=input("Enter your city:")
# print(f"My name is {name} and my course is {course} and my city is {city}")
#
# # 4. Write a program to display the Python version installed in the system.
#
#
#
# # 5.Write a program to print multiline text using triple quotes.
#
# name=input("Enter your name:")
# course=input("Enter your course:")
# city=input("Enter your city:")
# print(f"""My name is {name}
# My course is {course}
# My city is {city}""")
#
# # 6. Write a program demonstrating indentation of importance.
#
# # even or odd program
# def even_or_odd(num):
#     if num % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")
# even_or_odd(5)
# even_or_odd(6)
#
# # error because of wrong indentation
# # def even_or_odd(num):
# # if num % 2 == 0:
# # print("Even")
# # else:
# # print("Odd")
#
# # 7. Write a program of printing values using separator and end parameters.
# #
# # fruits=[str(x) for x in input("Enter your fruits:").split()]
# # print(fruits,sep="!")

# import sys
# print(sys.version)
# from platform import python_version
# print(python_version())
#
# import keyword
# print("Python Keywords:")
# print(keyword.kwlist)
# print(len(keyword.kwlist))