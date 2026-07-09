# # 10. Write a Python program to create a dictionary of 5 students and their marks. Display all keys and values.
#
# # Create a dictionary of 5 students and their marks
# students = {
#     "Alice": 85,
#     "Bob": 92,
#     "Charlie": 78,
#     "David": 88,
#     "Emma": 95
# }
#
# print("Student Names and Marks:\n")
#
# for name, marks in students.items():
#     print(f"Name:", name,"\n" "Marks:", marks,"\n")
#
#
# # 11. Write a Python program to add a new key-value pair and delete an existing key from a dictionary?
#
#
# # Create a dictionary
# students = {
#     "Alice": 85,
#     "Bob": 92,
#     "Charlie": 78
# }
#
# print("Original Dictionary:")
# print(students)
#
# # Add a new key-value pair
# students["David"] = 88
#
# print("\nDictionary after adding a new student:")
# print(students)
#
# # Delete an existing key
# del students["Bob"]
#
# print("\nDictionary after deleting 'Bob':")
# print(students)
# #
#
# # 12. Write a Python program to search for a specific key in a dictionary.
#
# students = {
#     "Alice": 85,
#     "Bob": 92,
#     "Charlie": 78,
#     "David": 88
# }
#
# key = input("Enter student name to search: ")
#
# marks = students.get(key)
# print(marks)
# if marks is not None:
#     print("Key found.")
#     print("Marks:", marks)
# else:
#     print("Key not found.")
#
#
# # 13. Write a Python program to count the total number of keys in a dictionary.
#
#
# students = {}
#
# n = int(input("Enter the number of students: "))
#
# for i in range(n):
#     name = input("Enter student name: ")
#     marks = int(input("Enter marks: "))
#     students[name] = marks
#
# print("\nDictionary:", students)
# print("Total number of keys:", len(students))
#
#
# # 14. Write a Python program to merge two dictionaries in to one.
#
# # First dictionary
# dict1 = {
#     "Alice": 85,
#     "Bob": 92
# }
#
# # Second dictionary
# dict2 = {
#     "Charlie": 78,
#     "David": 88
# }
#
# # Merge dictionaries
# dict1.update(dict2)
#
# print("Merged Dictionary:")
# print(dict1)
#
#
# # 15. Write a Python program to find the maximum and minimum value in a dictionary of numbers.
#
# # Create a dictionary
# numbers = {
#     "A": 45,
#     "B": 78,
#     "C": 23,
#     "D": 90,
#     "E": 56
# }
#
# # Find maximum and minimum values
# max_value = max(numbers.values())
# min_value = min(numbers.values())
#
# print("Maximum value:", max_value)
# print("Minimum value:", min_value)
#
#
# # 16. Write a Python program to create a dictionary from two lists (one of keys and one of values).
#
# # List of keys
# keys = ["A", "B", "C", "D", "E"]
#
# # List of values
# values = [10, 20, 30, 40, 50]
#
# # Create dictionary
# dictionary = dict(zip(keys, values))
#
# print("Dictionary:")
# print(dictionary)
#
#
# keys = ["A", "B", "C", "D"]
# values = [10, 20, 30, 40]
#
# dictionary = {}
#
# for i in range(len(keys)):
#     dictionary[keys[i]] = values[i]
#
# print(dictionary)
#
#
#
# # 17. Write a Python program to sort a dictionary by its keys.
#
# students = {
#     "Charlie": 78,
#     "Alice": 85,
#     "David": 88,
#     "Bob": 92
# }
#
# sorted_dict = dict(sorted(students.items()))
#
# print(sorted_dict)

#
#
#
# # 18. Write a Python program to sort a dictionary by its values.
#
# students = {
#     "Alice": 85,
#     "Bob": 92,
#     "Charlie": 78,
#     "David": 88
# }
#
# sorted_items = sorted(students.items(), key=lambda x: x[1], reverse=True)
#
# for key, value in sorted_items:
#     print(key, ":", value)

#
#
#
# # 19. Write a Python program to reverse a dictionary (swap keys and values).
#
# # Create a dictionary
# students = {
#     "Alice": 85,
#     "Bob": 92,
#     "Charlie": 78,
#     "David": 88
# }
#
# # Reverse the dictionary
# reversed_dict = {}
#
# for key, value in students.items():
#     reversed_dict[value] = key
#
# print("Original Dictionary:")
# print(students)
#
# print("\nReversed Dictionary:")
# print(reversed_dict)
#
#
# # 20. Write a Python program to create a nested dictionary for employee details.
#
# # Create a nested dictionary
# employees = {
#     "E101": {
#         "Name": "Alice",
#         "Age": 25,
#         "Salary": 50000
#     },
#     "E102": {
#         "Name": "Bob",
#         "Age": 30,
#         "Salary": 60000
#     },
#     "E103": {
#         "Name": "Charlie",
#         "Age": 28,
#         "Salary": 55000
#     }
# }
#
# print("Employee Details:")
#
# for emp_id, details in employees.items():
#     print("\nEmployee ID:", emp_id)
#     for key, value in details.items():
#         print(key, ":", value)
# #
#
#
# # 21. Write a Python program to calculate the average of all values in a dictionary.
#
# # Create a dictionary
# marks = {
#     "Alice": 85,
#     "Bob": 92,
#     "Charlie": 78,
#     "David": 88
# }
#
# # Calculate average
# average = sum(marks.values()) / len(marks)
#
# print("Average of values:", average)
# #
#
# # 22. Write a Python program to find the key with the highest value in a dictionary.
#
# marks = {
#     "Alice": 85,
#     "Bob": 92,
#     "Charlie": 78,
#     "David": 88
# }
#
# highest_key = ""
# highest_value = 0
#
# for key, value in marks.items():
#     if value > highest_value:
#         highest_value = value
#         highest_key = key
#
# print("Key with the highest value:", highest_key)
# print("Highest value:", highest_value)
# #
#
# # 23. Write a Python program to check if two dictionaries are equal.
#
# dict1 = {}
# dict2 = {}
#
# n = int(input("Enter the number of elements in first dictionary: "))
#
# print("Enter first dictionary:")
# for i in range(n):
#     key = input("Enter key: ")
#     value = input("Enter value: ")
#     dict1[key] = value
#
# m = int(input("\nEnter the number of elements in second dictionary: "))
#
# print("Enter second dictionary:")
# for i in range(m):
#     key = input("Enter key: ")
#     value = input("Enter value: ")
#     dict2[key] = value
#
# if dict1 == dict2:
#     print("\nBoth dictionaries are equal.")
# else:
#     print("\nBoth dictionaries are not equal.")
#
#
#
# # 24. Write a Python program to convert a dictionary in to a list of tuples .
#
# # Create a dictionary
# students = {
#     "Alice": 85,
#     "Bob": 92,
#     "Charlie": 78,
#     "David": 88
# }
#
# # Convert dictionary to list of tuples
# tuple_list = list(students.items())
#
# print("List of Tuples:")
# print(tuple_list)
#
#
# # 25. Write a Python program to count the frequency of each word in a sentence using a dictionary.
#
# sentence = input("Enter a sentence: ") + " "
#
# word = ""
# frequency = {}
#
# for ch in sentence:
#     if ch != " ":
#         word += ch
#     else:
#         if word in frequency:
#             frequency[word] += 1
#         else:
#             frequency[word] = 1
#         word = ""
#
# print("\nWord Frequencies:")
#
# for word, count in frequency.items():
#     print(word, ":", count)
#
#
#
# # Input sentence
sentence = input("Enter a sentence: ")

# Split sentence into words
words = sentence.split()

frequency = {}

# Count word frequency
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("\nWord Frequencies:")

for word, count in frequency.items():
    print(word, ":", count)