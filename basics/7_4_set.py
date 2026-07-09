# 11. Write a Python program to create a set of 10 numbers and print all elements using a loop

# def print_set(numbers):
#     print("Elements in set are: ")
#     for number in numbers:
#         print(number)
# numbers=set()
# for i in range (1,11):
#     num=int(input(f"Enter number {i}:"))
#     numbers.add(num)
# print(numbers)
# print_set(numbers)

# 12. Write a Python program to add a new element to a set and remove an existing element.

# st={1,4,5,6}
# for i in [1,3,7,8]:
#     st.add(i)
# print(st)
# st.remove(1)
# st.discard(10)
# print(st)


# 13. Write a Python program to find the union and intersection of two sets.

# st1={1}
# st2={1,2}
# new_st=st1.union(st2) # new set created and stores union
# print(new_st)
# new_st=st1.intersection(st2)
# print(new_st)

# 14. Write a Python program to remove all duplicate values from a list using a set.

# ls=[1,2,1,3,3,4,5,5]
# st=set(ls)
# print(st)

# 15. Write a Python program to count the number of elements in a set.

# st={1,2,3,4,5}
# # count=len(st)
# # print(count)
# count=0
# for ele in st:
#     count+=1
# print(count)

# 16. Write a Python program to convert a set into a list and sort the elements.

# st={2,1,8,3,6,1}
# ls=list(st)
# for idx in range(len(ls)):
#     for idx1 in range(idx+1,len(ls)):
#         if ls[idx]>ls[idx1]:
#             ls[idx],ls[idx1]=ls[idx1],ls[idx]
# print(ls)

# 17. Write a Python program to find the common elements among three sets.

# st1={1,2,3,4}
# st2={2,3,4}
# st3={2,5,6,3}
# st4={2}
# common=st1.intersection(st2,st3,st4)
# print(common)

# 18. Write a Python program to remove all elements from a set one by one using a loop.

st={1,2,3,4,5}
# for ele in st:
#     st.remove(ele)
# print(st)

# for ele in st:
#     st.pop()
# print(st)

# for ele in st.copy():
#     st.remove(ele)
# print(st)

# st.clear()
# print(st)










# 19. Write a Python program to check if all elements of one set exist in another set.

# set1 = {1, 2, 3}
# set2 = {1, 2, 3, 4, 5}
#
# if set1.issubset(set2):
#     print("All elements of set1 exist in set2.")
# else:
#     print("Some elements of set1 do not exist in set2.")


# 20. Write a Python program to compare two sets and print which one is larger.

# set1 = set(map(int, input("Enter elements of set1: ").split()))
# set2 = set(map(int, input("Enter elements of set2: ").split()))
#
# if len(set1) > len(set2):
#     print("Set1 is larger.")
# elif len(set2) > len(set1):
#     print("Set2 is larger.")
# else:
#     print("Both sets are of equal size.")



# 21. Write a Python program to generate a set of even numbers upto n

# n = int(input("Enter a number: "))
#
# even_set = set()
#
# for i in range(2, n + 1, 2):
#     even_set.add(i)
#
# print("Set of even numbers:", even_set)



# 22. Write a Python program to create a set of squares of the first n natural numbers

# n = int(input("Enter the value of n: "))
#
# square_set = {i ** 2 for i in range(1, n + 1)}
#
# print(square_set)