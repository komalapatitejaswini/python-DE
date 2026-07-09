
# 1. odd_even counting problem

# tp=(1,2,3,4,5)
# odd_num=0
# even_num=0
# for ele in tp:
#     if ele%2==0:
#        even_num+=1
#     else:
#         odd_num+=1
# print(f"Even numbers in tuple are: {even_num} and odd numbers in tuple are: {odd_num}")

# 2. check if all elements in one set exists in another set

# st={1,2,3}
# st2={1,3,2,4,5}
# print(st.issubset(st2))

# 3. compress string problem

# s="aabcccccaaa"
# count=1
# s2=""
# for idx in range(len(s)-1):
#     if s[idx]==s[idx+1]:
#         count+=1
#     else:
#         s2 += s[idx] + str(count)
#         count=1
# s2+=s[idx]+str(count)
# print(s2)


# 4.sort dictionary by keys

# d1={"b":3,"a":1,"c":2}
# sort_key=sorted(d1.items())
# print(dict(sort_key))
#
# # sort dict by values in descending order
#
# sort_value=sorted(d1.items(), key=lambda x:x[1], reverse=True)
# print(dict(sort_value))
#
# # sort dict by values in ascending order
#
# sort_value=sorted(d1.items(), key=lambda x:x[1])
# print(dict(sort_value))

# 5.Merge dictionaries(Multiply values if same keys)

# d1={"a":10,"b":20}
# d2={"a":5,"c":15}
# for key,value in d2.items():
#     if key in d1.keys():
#         d1[key]=d1[key]*value
#     else:
#         d1[key]=value
# print(d1)

# 6.convert snake_case to camelCase

# s1="hello_world"
# s2=("")
# idx=0
# while idx<len(s1):
#     if s1[idx]=="_":
#         idx += 1
#         s2+=s1[idx].upper()
#     else:
#         s2+=s1[idx]
#     idx+=1
# print(s2)

# 7. Reverse each word problem

# sentence = "hello world"
# words = sentence.split()
# for word in words:
#     word=word[::-1]
#     print(word,end=" ",)

# 8. key searching problem

# d={"age":25,"name":"Teja","curr_loc":"bengaluru"}
# print(d.get("name","key not found"))

# 9. square counting problem

# ls=[1,2,3,4]
# mp=map(lambda x:x**2,ls)
# print(list(mp))

# 10. Find distinct count

lst=[1,2,2,3,4,4,4,5]
st=set(lst)
count=0
for each in st:
    count+=1
print(count)