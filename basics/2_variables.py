# 1.

# a = "10"
# b = 5
# print(a + str(b))

#2.

# x = 5
# x = "Hello"
# print(type(x))

#3.

# x = True
# y = 5
# print(x + y)

#4.Arithmetic operations on 2 numbers

# num1=int(input("Enter a number"))
# num2=int(input("Enter another number"))
# result=num1+num2
# print(result)
# result=num1-num2
# print(result)
# result=num1*num2
# print(result)
# result=num1/num2
# print(result)
# result=num1//num2
# print(result)
# result=num1%num2
# print(result)
# result=num1**num2
# print(result)

#5.del a variable

# a=4
# # del a
# print(a)

# 6.checking datatype after converting to int

# num=int(input("Enter a number"))
# print(type(num))

# 7. value changed from int to string

# num=44
# print(type(num))
# num="Teja"
# print(type(num))

# 8.swap variables without 3rd variable

# num1=4
# num2=6
# num1,num2=num2,num1
# print(num1,num2)

# 9.difference between local variable  and  global variable

x=12
print(f"global x is:{x}")
def fun1():
    # global a
    a=10
    print(f"local a is:{a}")
    print(f"global x is:{x}")
    def fun2():
        b=14
        print(f"local b is:{b}")
        print(f"enclosed a is:{a}")
        print(f"global x is:{x}")
    fun2()
fun1()
# print(a)

x = 10 # Global -- common for all funcs
def func():
    x1 = 11
    def func2():
        # x = 10 #for this func--> this x is local, x1 is enclosed, x- global(common for all funcs)
        print(x1)
    func2()
func()

# 10.program to rotate three variables:

# a=int(input("Enter 1st number:"))
# b=int(input("Enter 2nd number:"))
# c=int(input("Enter 3rd number:"))
# # a=10
# # b=20
# # c=30
# a,b,c=c,a,b
# print(a,b,c)


# 11.program to check whether two variables refer to the same memory location.

# a=10
# b=10
# c=10
# print(id(a),id(b),id(c))

# 12. program to demonstrate dynamic typing by changing the type of a variable multiple times

# a=10
# print(a)
# print(type(a))
# a=10.10
# print(a)
# print(type(a))
# a="Teja"
# print(a)
# print(type(a))
# a=True
# print(a)
# print(type(a))

# 13.program to check memory address of variables using id().

# a=10
# b=20
# print(id(a))
# print(id(b))

# a=10
# print(id(a))
# a=20
# print(id(a))

# 14. Write a program to check whether two variables are equal using both == and is, and explain the difference.

# x = 10
# y = 10
#
# if x == y:
#     print("true")
# else:
#     print("false")

# print(x is y)
# print(x == y)
# print(id(x))
# print(id(y))

# x=[1,2,3]
# y=[1,2,3]
# if x==y:
#     print("x and y are equal")
# else:
#     print("x and y are not equal")
# if x is y:
#     print("x and y are equal")
# else:
#     print("x and y are not equal")
#
#
#
# def check_odd_even(num):
#     if num % 2 ==0:
#         return "Even"
#     else:
#         return f"odd {num}"
#
# num = int(input("enter number: "))
# res = check_odd_even(num)
# print(res)




