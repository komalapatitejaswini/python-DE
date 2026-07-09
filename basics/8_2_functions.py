# recursion to convert nested list to flattened list

def flatten(nested_list):
    flat= []
    for item in nested_list:
        if isinstance(item,list):
            flat.extend(flatten(item))
        else:
            flat.append(item)
    return flat
nested_list=[1,2,[3,4],[5,6,[7,8,[9,10]]],11,12]
print(flatten(nested_list))

# 11.demonstrate the use of a global variable inside a function

x=30
def outer():
    # x=20
    global x
    x+=10
    def inner():
        # x=10
        return x
    return inner
print(outer()())


# 12. return both the quotient and remainder of two numbers

# def quo_rem(num1, num2):
#     quo=num1//num2
#     rem=num1%num2
#     return quo,rem
# num1=int(input("Enter first number: "))
# num2=int(input("Enter second number: "))
# print(quo_rem(num1, num2))

# 13.Take one list of integers, return a new list containing the square of each number using map() and lambda

# mp=map(lambda x:x**2,[1,2,3,4,5])
# print(list(mp))

# num=int(input("Enter a number: "))
# mp=map(lambda x:x**2,range(1,num+1))
# print(list(mp))

# 14.extract only the even numbers using filter() and lambda

# fl=filter(lambda x:x%2==0,[1,3,5,7,8,2])
# print(list(fl))
# num=int(input("Enter a number: "))
# fl=filter(lambda x:x%2==0,range(num+1))
# print(f"even numbers till {num} are: {list(fl)}")

# 15.one list of names, use filter()and lambda to extract names that start with a vowel

# fl=filter(lambda x:x[0] in "AEIOUaeiou",["Teja","eva","Sai","Aadhya"])
# print(list(fl))

# 16.function to calculate the power of a number using recursion

def power(x, n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        return x * power(x, n - 1)
x=int(input("Enter a number: "))
n=int(input("Enter power number: "))
print(power(x,n))