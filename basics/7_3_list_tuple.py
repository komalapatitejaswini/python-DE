# tp=(each**2 for each in [1,2,3,4,5])
# print(tp)
# print(tp.__next__())
# print(tuple(tp))

# 1.create a list of 10 integers and print all elements using a loop

# ls=[]
# for each in range(1,11):
#     ls.append(each)
# print(ls)

# 2. find the sum of all elements in a list using a loop

# ls=eval(input("Enter a list: "))
# sum=0
# for each in ls:
#     sum+=each
# print(sum)

# 3.count how many even and odd numbers are in a list
# ls=eval(input("Enter a list: "))
# even=0
# odd=0
# for each in ls:
#     if each%2==0:
#         even+=1
#     else:
#         odd+=1
# print(f"even numbers in list are: {even} and odd numbers in list are: {odd}")

# 4.search for a given element in a list and display its position
# ls=input("Enter a list: ").split(",")
# print(type(ls))
# search_ele=input("Enter the element to be searched in the list: ")
# idx=ls.index(search_ele)
# print(idx)

# 5. Insert an element at a given position in a list

# ls=input("Enter a list: ").split(",")
# position=int(input("Enter a position where the element need to be inserted: "))
# value=input("Enter a value to be inserted: ")
# ls.insert(position,value)
# print(ls)

# 6.merge two lists in to a single list
# lst1=input("Enter a list: ").split(",")
# lst2=input("Enter another list: ").split(",")
# lst3=lst1+lst2
# print(lst3)

# 7.remove duplicate elements from a list

# lst=input("Enter a list: ").split(",")
# st=set(lst)
# print(st)

# 8.create a nested list and print each element separately
# ls=[[1,2],[3,4]]
# ls1=[]
# for each in ls:
#     for ele in each:
#         ls1.append(ele)
# print(ls1)

# 9.delete all occurrences of a given element from a list
# ls=[1,1,3,5,1,1]
# st=set(ls)
# st.remove(1)
# print(list(st))
#
# s={1,"a","b","c"}
# print(s)
# s.pop()
# print(s)

# 10.count how many even and odd numbers are in a tuple
# tp=tuple(input("Enter a tuple: ").split(","))
# # print(type(tp))
# even=0
# odd=0
# for each in tp:
#     if int(each)%2==0:
#         even+=1
#     else:
#         odd+=1
# print(f"even numbers in tuple are: {even} and odd numbers in tuple are: {odd}")

# 11.search for a given element in a tuple and display its index

# tp=tuple(input("Enter a tuple: ").split(","))
# ele=input("Enter a element for which you want index: ")
# idx=tp.index(ele)
# print(idx)

# 12.reverse a list using a loop
# ls=input("Enter a list: ").split(",")
# ls1=[]
# for idx in range(-1,-len(ls)-1,-1):
#     # print(ls[idx])
#     ls1.append(ls[idx])
# print(ls1)

# 13.sort a list in ascending order without using built-in functions

# ls=[2,1,5,4,3,1,2]
# for idx in range(len(ls)):
#     for idx2 in range(idx+1,len(ls)):
#         if ls[idx] > ls[idx2]:
#             ls[idx2],ls[idx] = ls[idx],ls[idx2]
# print(ls)

# 14.split a list into two lists(even numbers and odd numbers)

# ls=[1,2,3,4,5,6,8]
# ls_even=[]
# ls_odd=[]
# for each in ls:
#     if each%2==0:
#         ls_even.append(each)
#     else:
#         ls_odd.append(each)
# print(ls_even)
# print(ls_odd)

# 15. find the second-largest number in a list

# ls=[2,1,4,1,2,8,11,11,6]
# print(ls)
# for each in ls:
#     c=ls.count(each)
#     if c>1:
#         ls.remove(each)
# print(ls)
# for idx in range(len(ls)):
#     for idx1 in range(idx+1,len(ls)):
#         if ls[idx]>ls[idx1]:
#             ls[idx],ls[idx1]=ls[idx1],ls[idx]
# print(ls)
# print(ls[-2])

# 16.count the frequency of each element in a list

# lst = [1, 2, 3, 2, 1, 4, 2, 5, 1]
# visited = []
# for ele in lst:
#     if ele not in visited:
#         count = 0
#         for j in lst:
#             if ele == j:
#                 count += 1
#         print(ele, ":", count)
#         visited.append(ele)

# 17.check whether a list is a palindrome or not

# lst=[1,2,3,2,1]
# print(lst)
# rev_lst=[each for each in lst[::-1]]
# print(rev_lst)
# if lst==rev_lst:
#     print("palindrome")
# else:
#     print("not palindrome")



# l = [10,4,5,7,11,10,14,10,12,10]
# for _ in range(l.count(10)):
#     l[l.index(10)] = 100
# print(l)
#
#
# l = [10,4,5,7,11,10,14,10,12,10]
# for _ in range(4):
#     l[l.index(10)] = 100
# print(l)

# l = ["flow", "flower", "flix", "flex"]
# prefix = ""
# for i in range(len(l[0])):
#     ch = l[0][i]
#     for word in l:
#         if i >= len(word) or word[i] != ch:
#             print(prefix)
#             exit()
#     prefix += ch
# print(prefix)
#
text_original=['rate','mate','date','eat']
prefix='sub'
# sufix='less'
# print("previous no.",text_original)
for each in text_original:
    new_text=prefix+each
    text_original.append(new_text)
    # new_sufix=each+sufix
# print(new_sufix)
print(text_original)
