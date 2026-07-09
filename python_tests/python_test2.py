# 1.count occurrences of character
# str=input("Enter a string: ")
# char=input("Enter a character: ")
# count=0
# for each in str:
#     if each==char:
#         count+=1
# print(count)

# 2.check anagram problem
# s1=input("Enter a string: ")
# s2=input("Enter another string: ")
# if len(s1)==len(s2):
#     for each in s1:
#         if s1.count(each)!=s2.count(each):
#             print("not anagrams")
#             break
#     else:
#         print("Anagrams")
# else:
#     print("Not Anagrams")

# 3.extract numbers from string

# string=input("Enter a string: ")
# digits={'0','1','2','3','4','5','6','7','8','9'}
# num=[]
# for each in string:
#     if each in digits:
#         num.append(each)
# print(num)

# 4.Reverse a list using a loop

# ls=input("Enter a list: ").split(",")
# ls1=[]
# for each in ls[::-1]:
#     ls1.append(each)
# print(ls1)

# 5.sort a list in ascending order

# ls=input("enter a list: ").split(",")
# for idx in range(len(ls)):
#     for idx1 in range(idx+1,len(ls)):
#         if ls[idx]>ls[idx1]:
#             ls[idx],ls[idx1]=ls[idx1],ls[idx]
# print(ls)

# 6.create a set of squares of first n natural numbers

# n=int(input("Enter a number: "))
# ls=[]
# for each in range(1,n+1):
#     ls.append(each**2)
# print(ls)

# 7.reverse a dictionary

# dict={"a":1,"b":2,"c":3}
# rev={value: key for key,value in dict.items()}
# print(rev)

# 8.count frequency of each word in a sentence using a dictionary

# sentence = "apple banana apple cherry banana apple"
# words = sentence.split()
# word_count = {}
# for word in words:
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1
# print(word_count)

# 9.sum and average of elements in list

# ls=[10,20,30,40,50]
# sum=0
# for each in ls:
#     sum+=each
# avg=sum/len(ls)
# print(f"sum of numbers is: {sum} and average of numbers is: {avg} ")

# 10.find 2nd highest key in dictionary

# dict={"Alice":85,"Bob":92,"Charlie":88,"David":95}
# # for key in dict.keys():
# #     print(key)
# second_highest_key=sorted(dict)[-2]
# print(second_highest_key)













