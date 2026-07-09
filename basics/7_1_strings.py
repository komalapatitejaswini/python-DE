# 10.accept a string from the user and display it in reverse order

# s=input("Enter a string: ")
# s1=""
# for each in range(len(s)-1,-1,-1):
#     # print(s[each])
#     s1=s1+s[each]
# print(s1)
# print(s[::-1])

# 11.count the number of vowels and consonants in a given string
#
# s=input("Enter a string: ")
# v=0
# c=0
# invalid=False
# for each in s:
#     if 'a' <= each <= 'z' or 'A' <= each <= 'Z':
#         if each in "AEIOUaeiou":
#             v+=1
#         else:
#             c+=1
#     else:
#         invalid=True
# if invalid:
#     print("Enter alphabet between A and Z/a and z")
# else:
#     print("Vowels are: ",v)
#     print("Consonants are: ",c)

# 12. check whether a substring exists in a given string


# s=input("Enter a string: ")
# for i in s:
#     print(i)
# for i in range(0,len(s)-1):
#     ns=s[i]+s[i+1]
#     print(ns)
# for i in range(0,len(s)-2):
#     ns=s[i]+s[i+1]+s[i+2]
#     print(ns)

# print all the substrings
# s=input("Enter a string: ")
# res=[]
# for i in range(len(s)):
#     for j in range(i,len(s)):
#         res.append(s[i:j+1])
# print(res)

# s=input("Enter a string: ")
# sub_str=input("Enter a sub string: ")
# if sub_str in s:
#     print("Substring is present in the string")
# else:
#     print("Substring is not present in the string")


# 13. print the first and last character of a string.

# s=input("Enter a string: ")
# print("First character of string: ",s[0])
# print("Last character of string: ",s[-1])

# 14.check whether a given string is a palindrome or not

# s=input("Enter a string: ")
# s1=""
# for idx in range(len(s)-1,-1,-1):
# 	s1+=s[idx]
# print(s1)
# if s1==s:
# 	print("The string is palindrome")
# else:
# 	print("The string is not palindrome")
# if s==s[::-1]:
# 	print("The string is palindrome")
# else:
#     print("The string is not palindrome")

# 15.replace all spaces in a string with hyphens(-)

# s=input("Enter a string: ")
# s1=""
# for each in s:
#     if each==" ":
#         each="-"
#         s1+=each
#     elif each != " ":
#             s1 += each
# print(s1)

# 16.convert all Lowercase letters in a string to uppercase

# s=input("Enter a string: ")
# res=""
# for ch in s:
#     if 'a'<=ch<='z':
#         res+=chr(ord(ch)-32)
#     else:
#         res+=ch
# print(res)


# 17.count the number of words in a sentence

# s=input("Enter a string: ")
# s1=s.strip()
# count=1
# for each in s1:
#     if each==" ":
#         count+=1
# print(count)

# 18.split a sentence into words and print each word on a new line

s=input("Enter a string: ")
##Hello world
s1=s.strip()
each_word=""
for idx in range(len(s1)):
    if s[idx] != " " or  idx ==0:
        each_word=each_word+s[idx]
    if s[idx-1] == " ":
        print()
    print(each_word,end="")
    each_word = ""

# sentence=input("Enter a sentence: ")
# word=""
# for ch in sentence:
#     if ch!=" ":
#         word+=ch
#     else:
#         print(word)
#         word=""
# print(word)

# 19. frequency of each character in a string
# string=input("Enter a string: ")
# visited=""
# count=0
# for char in string:
#     if char not in visited:
#         count=0
#         for c in string:
#             if c==char:
#                 count+=1
#         print(char,":",count)
#         visited+=char











