# 16.first 20 odd numbers
# for num in range(0,40):
#     if num%2!=0:
#         print(num)

# 17.sum of first n natural numbers
# n=int(input("Enter a number: "))
# sum=0
# for number in range(n+1):
#     sum=sum+number
# print(sum)

# 18.multiplication table of a given number(upto10)
# all tables till 10
# number=int(input("Enter a number: "))
# if 1<=number<=10:
#     for number in range(1,number+1):
#         for num in range(1,11):
#             mul=number*num
#             print(f"{number} x {num} = {mul}")
# else:
#     print("Invalid input- enter a number between 1 and 10")

# single table
# n = int(input("Enter a number: "))
# for num in range(1,11):
#     mul = n * num
#     print(f"{n} x {num} = {mul}")

# 19.print numbers from 1 to 10 check whether it is even or odd
# for num in range(1,11):
#     if num % 2 == 0:
#         print(f"{num} is even")
#     else:
#         print(f"{num} is odd")

# 20.Python program to calculate the power of a number

# num=int(input("Enter a number: "))
# power=int(input("Enter a power: "))
# p=1
# for _ in range(power):
#     p=p*num
# print(p)

# 21.average of n numbers entered by the user
# lst=eval(input("Enter a list: "))
# sum=0
# for i in range (len(lst)):
#     sum=sum+lst[i]
#     avg=sum/len(lst)
# print("The Average is",avg)

# 22.factorial of a given number using a while loop

# num=int(input("Enter a number: "))
# prod=1
# for numbers in range (1,num+1):
#     prod=prod*numbers
# print("Factorial is: ",prod)

# 23.print all prime numbers between 1 and 100

# num=int(input("Enter a number: "))
# for ele in range(2,num//2+1):
#     if num % ele == 0:
#         print(f"Element {num} is not a prime number")
#         break
# else:
#     print(f"Element {num} is a prime number")

# 24. reverse a given number using a loop
# num=int(input("Enter a number: "))
# res_num=0
# while num>0:
#     rem=num%10
#     res_num=res_num*10+rem
#     num=num//10
# print(res_num)

# 25.count the number of digits in a given number.
# num=int(input("Enter a number: "))
# count=0
# while(num>0):
#     rem=num%10
#     count+=1
#     num=num//10
# print(count)

# 26.palindrome or not

# num=int(input("Enter a number: "))
# temp=num
# res_num = 0
# while num>0:
#     rem=num%10
#     res_num=res_num*10+rem
#     num=num//10
# print(res_num)
# if res_num==temp:
#     print("Palindrome")
# else:
#     print("Not Palindrome")


# 27.print the sum of digits of a given number

# num=int(input("Enter a number: "))
# res_sum=0
# while num>0:
#     rem=num%10
#     res_sum+=rem
#     num = num // 10
# print(res_sum)


# whether a number is power of 3 or not
# num=int(input("Enter a number: "))
# c=0
# while num>1:
#     c+=1
#     num=num/3
#     if c==3:
#         print("yes")
#         break
# else:
#         print("no")



