# 1. Count occurrences of a specific character
# string=input("Enter a string: ")
# char=input("Enter a character: ")
# print(f"The count of {char} is {string.count(char)}")

# 2.Replace all occurrences of a character with another
# string=input("Enter a string: ")
# original_char=input("Enter a character you want to replace: ")
# new_char=input("Enter another character with which you want to replace: ")
# print(string.replace(original_char,new_char))

# 3. Check if a string contains a given substring
# string=input("Enter a string: ")
# substring=input("Enter a substring: ")
# if substring in string:
#     print(True)
# else:
#     print(False)

# 4. Swap the first and last characters in a string
# string=input("Enter a string: ")
# if len(string)>1:
#     res_string=string[-1]+string[1:-1]+string[0]
#     print(res_string)
# else:
#     print("String is of length 1 or less so no swap.")

# 5.Concatenate two strings
# s1=input("enter first string: ")
# s2=input("enter second string: ")
# result=s1+" "+s2
# print(result)

# 6.Count the number of words in a string
# string=input("Enter a string: ")
# string1=string.strip()
# words=string1.split(" ")
# word_count=len(words)
# print(word_count)

# 7. Reverse each word in the string separately
# sentence=input("Enter a sentence: ")
# words=sentence.split()
# a=[]
# for word in words:
#     a.append(word[::-1])
# res=" ".join(a)
# print(res)

# 8. Convert string to title case
# string=input("Enter a string: ")
# s1=string.title()
# print(string)
# print(s1)
# print(id(string))
# print(id(s1))

# ls=[1,2,3,4,5]
# ls.append(6)
# print(ls)
# # print(ls1)
# print(id(ls))
# # print(id(ls1))

# 9. Remove punctuation characters from a string
# string=input("Enter a string: ")
# punctuation="!"
# s=""
# for ch in  string:
#     if ch!=punctuation:
#         s += ch
# print(s)

# 10.Check if two strings are anagrams

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

# 11. Find the first non-repeating character in a string
# s=input("Enter a string: ")
# for item in s:
#     if s.count(item)==1:
#         print(item)
#         break
# 12. Longest Palindromic Substring Problem
# s=input("Enter a string: ")
# res=[]
# for i in range(len(s)):
#     for j in range(i,len(s)):
#         res.append(s[i:j+1])
# print(res)
# for each in res:
#     if len(each)>1:
#         if each == each[::-1]:
#             print(f"{each} is palindrome")


# 13.Count how many times a substring appears in a string

# s=input("Enter a string: ")
# sub_string=input("Enter a sub string: ")
# # sub_string_count=s.count(sub_string)
# # print((f"{sub_string_count} times substring appears in string." ))
#
# # for overlapping strings
# count=0
# for i in range(len(s)):
#     if s[i:i+len(sub_string)]==sub_string:
#         count+=1
# print(count)

# 14.Title Case Except Stop Words Problem

# s=input("Enter a string: ")
# word_list=s.split()
# print(word_list)
# stop_words={"and","the","of"}
# res_word=""
# first_word=word_list[0].title()
# for each_word in word_list[1::]:
#     if each_word not in stop_words:
#         res_word+=each_word.title()+" "
#     else:
#         res_word+=each_word+" "
# print(first_word+" "+res_word)

# 15.Validate Palindrome Ignoring Non-Alphaeus Problem

# s=input("Enter a string: ")
# print(not s.isalnum())



# 16. Extract all digits from a string as a number

# s=input("Enter a string: ")
# res=""
# for ch in s:
#     if ch.isdigit():
#         res+=ch
# print(int(res))

string=input("Enter a string: ")
num=""
for each in string:
    if each in "0123456789":
        num+=each
print(int(num))


