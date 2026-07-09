# 7. Write a Python program to create an array of integers and display its elements.

# import array as arr
# st=arr.array("b",[1,2,3,4,5])
# print(st)

# 8. Write a Python program to append and remove elements from an array.

# import array as arr
# st=arr.array("b",[1,2,3,4,5])
# st.append(6)
# print(st)
# st.remove(5)
# print(st)


# 9. Write a Python program to find the sum and average of elements in an array.

# import array as arr
# st=arr.array('i',[1,2,3,4,5])
# sum=0
# for each in st:
#     sum+=each
# avg=sum/len(st)
# print(sum,avg)


# 10. Write a Python program to perform shallow and deep copy in a list using the copy module.

# import copy
# shallow copy

# ls=[1,"a",[1,2]]
# s_c=copy.copy(ls)
# ls[2].append(3)
# print(s_c)
# print(ls)
# print(id(ls[2]))
# print(id(s_c[2]))

# deep copy

# ls=[1,"a",[1,2]]
# d_c=copy.deepcopy(ls)
# ls[2].append(3)
# print(d_c)
# print(ls)
# print(id(ls[2]))
# print(id(d_c[2]))


# 11. Write a Python program to compare original and copied objects and display whether they Refer to the same memory location, check by both shallow and deep copy .

# # shallow copy
# import copy
# ls=[1,"a",[1,2]]
# s_c=copy.copy(ls)
# ls.append(5)
# print(s_c)
# print(ls)
#
# # mem address of nested list is copied so changes in org list are reflected in copied list
#
# ls[2].append(3)
# print(s_c)
# print(ls)
# print(id(ls[2]))
# print(id(s_c[2]))
#
# # deep copy
#
# ls=[1,"a",[1,2]]
# d_c=copy.deepcopy(ls)
# ls.append(5)
# print(d_c)
# print(ls)
#
# # nested list is assigned new memory in deep copy so changes in nested list are not reflected
#
# ls[2].append(3)
# print(d_c)
# print(ls)
# print(id(ls[2]))
# print(id(d_c[2]))





