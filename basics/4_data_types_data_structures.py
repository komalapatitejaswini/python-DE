# 1.Create a list of numbers and print all elements
# ls=[int(i) for i in input("enter a list separated by space ").split()]
# for ele in ls:
#     print(ele)

# 3. Write a program to find the data typeof a given variable.
# num=9
# print(type(num))
# num=9.9
# print(type(num))
# num=5j
# print(type(num))
# num=False
# print(type(num))
# name="Teja"
# print(type(name))
# ls=[1,3]
# print(type(ls))
# tp=(4)
# print(type(tp))
# tp=(4,)
# print(type(tp))
# st={1,2,3,4,5}
# print(type(st))
# dt={"name":"Teja","age":18,}
# print(type(dt))

# 5.Convert an integer to a string and print the result
# num=9
# print(num)
# print(type(num))
# x=str(num)
# print(x)
# print(type(x))

# 7.Convert a list into a tuple. Create a tuple and access its elements using indexing.
# # list to tuple
# ls=[1,2,3,4,5]
# x=tuple(ls)
# print(type(x))
# # create tuple and access by indexing
# tp=(2,5,6)
# print(tp[2])

# 8.Write a program to add elements to a list.

# list=[str(x) for x in input("Enter elements in the list:").split()]
# n=int(input("Enter number of elements to be added in the list:"))
# for i in range(n):
#     item=input(f"Enter the {i+1} element:")
#     list.append(item)
# print("The list is ",list)

# 9. Remove an element from a list.

# lst=[int(x) for x in input("Enter the list: ").split()]
# print(lst)
# rem=int(input("Enter the number to be removed:"))
# lst.remove(rem)
# print(lst)

# lst = [1,2,3,4]
# ele = 3
# lst.remove(4)
# print(lst)

# lst = eval(input("Enter list"))
# ele = int(input("enter number"))

# if ele in lst:
#     lst.remove(ele)
#     print(lst)
# else:
#     print("ELEMENT NOT PRESENT IN THE SEQUENCE!")
# lst1 = []
# for num in lst:
#     if num == ele:
#         continue
#     else:
#         lst1 += [num]
# print(lst1)

# 10.Create a set from a list and print unique elements.
# list=[int(x) for x in input("Enter the list: ").split()]
# print(list)
# st=set(list)
# print(st)

# 11. Create a dictionary and print all keys and values.

# dict={"Name":"Teja","Age":25}
# for key,value in dict.items():
#     print(key,value)

# 12.
# dict={"Name":"Teja","Age":25}
# for key,value in dict.items():
#     print(key,value)
# print(dict["Name"])
# print(dict["Age"])

# 13.
# for i in range(1,11):
#     print(i)

# 14.
# for i in range(2,20,2):
#     print(i)

#15.
# for i in range(10,0,-1):
#     print(i)

# 16.
# n=int(input("Enter a number:"))
# sum=0
# for i in range(1,n+1):
#     print(i)
#     sum += i
# print("sum of first n numbers : ",sum)

# 17.
# lst=eval(input("Enter a list: "))
# count=0
# for i in lst:
#     # print(i)
#     count=count+1
# print("Number of elements in list",count)

# 18.
# lst=eval(input("Enter a list: "))
# ele=int(input("Enter the element: "))
# if ele in lst:
#     print("Element is present in list")
# else:
#     print("Element is not present in list")

# 19.

# lst=eval(input("Enter a list: "))
# max_ele = lst[0]
# min_ele = lst[0]
# for i in range(len(lst)):
#     if lst[i]>max_ele:
#         max_ele = lst[i]
#     if lst[i]<min_ele:
#         min_ele = lst[i]
# print(max_ele)
# print(min_ele)

# lst=eval(input("Enter a list: "))
# for i in range(len(lst)-1):
#     if lst[i]>lst[i+1]:
#         lst[i],lst[i+1]=lst[i+1],lst[i]
# print(lst[len(lst)-1])

# 20.reverse a list

# lst=eval(input("Enter a list: "))
# rev_list=[]
# # lst.reverse()
# # for loop to find index
# for each in range(len(lst)-1,-1,-1):
#     # by index u fetch the element from lst and append to rev_lst
#     rev_list.append(lst[each])
# print(rev_list)

# print(range(2,-1,-1))
# for i in range(2,-1,-1):
#     print(i)

# slicing
# rev_list=[]
# for each in lst[::-1]:
#     rev_list.append(each)
# print(rev_list)

# list comprehension
# rev_list=[each for each in lst[::-1]]
# print(lst)
# print(rev_list)

# 21.duplicate elements in a list
# lst=eval(input("Enter a list: "))
# st=set()
# duplicates=set()
# for item in lst:
#     if item in st:
#         duplicates.add(item)
#     else:
#         st.add(item)
# print(list(duplicates))

# 22.Merge two lists

lst1=eval(input("Enter a list: "))
lst2=eval(input("Enter another list: "))
# res=[]
# for elem in lst1:
#     res.append(elem)
# for elem in lst2:
#     res.append(elem)
# print(res)

# res=lst1+lst2
# print(res)

# lst1.extend(lst2)
# print(lst1)

# res=[*lst1,*lst2]
# print(res)










