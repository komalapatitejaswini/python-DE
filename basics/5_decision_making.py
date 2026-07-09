# 1.check whether a number is positive, negative, or zero.

# num=int(input("Enter a number: "))
# if num>0:
#     print("positive")
# elif num<0:
#     print("negative")
# else:
#     print("zero")

# 2.check whether a person is eligible to vote

# age=int(input("Enter your age:"))
# if age<=0:
#     print("Your age must be greater than 0")
# elif age>=18:
#     print("You are eligible to vote")
# else:
#     print("You are not eligible to vote")

# 3.check grade based on marks

# marks=int(input("Enter marks:"))
# if marks<0 or marks>100:
#     print("enter valid marks between 0 and 100")
# elif 90<=marks<=100:
#     print("Grade A")
# elif 75<=marks<90:
#     print("Grade B")
# elif 50<=marks<75:
#     print("Grade C")
# else:
#     print("Fail")

# 4.check whether a year is a leap year or not.

# year=int(input("Enter year:"))
# if year%100==0 :
#     if year%400==0:
#         print("Entered century year is a leap year")
#     else:
#         print("Entered century year is not a leap year")
# elif year%4==0:
#     print("Entered year is a leap year")
# else:
#     print("Entered year is not a leap year")

# year=int(input("Enter year:"))
# if year%100==0 and year%400==0:
#         print("Entered century year is a leap year")
# elif year%100==0 and year%400!=0:
#         print("Entered century year is not a leap year")
# elif year%4==0:
#     print("Entered year is a leap year")
# else:
#     print("Entered year is not a leap year")

# 5. check login credentials (username & password)

# user_name = input("Enter userName:")
# pass_word = input("Enter password:")
#
# if user_name == "teja234" and pass_word == "Teja1233$":
#     print("Valid Credentials")
# else:
#     print("Invalid Credentials")

# 6.check whether a character is vowel or consonant

# char=input("enter character A-Z/a-z: ")
# if 'a'<= char <= 'z' or 'A'<= char <= 'Z':
#     # print("yes, this is alpha char")
#     if char in ('a','e','i','o','u','A','E','I','O','U'):
#         print("vowel")
#     else:
#         print("consonant")
# else:
#     print("Invalid Character!")

# 7.check if a number is divisible by both 3 and 5

# num=int(input("enter number: "))
# if num%3==0 and num%5==0:
#     print("Number is divisible by both 3 and 5.")
# else:
#     print("Number is not divisible by both 3 and 5.")

# 8.
# balance=int(input("enter balance: "))
# amount=int(input("enter amount: "))
# if amount<=0:
#     print("Enter valid amount")
# elif balance>=amount:
#     print("Allow withdrawal.")
# else:
#     print("Insufficient balance.")

# 9.

# day_type=input("Enter day_type weekend/weekday: ").lower()
# if day_type=="weekday":
#     print("Go to office.")
# elif day_type=="weekend":
#     activity_type=input("Enter activity type Party/Trip/movie: ").lower()
#     if activity_type=="party":
#         party_type=input("Enter party type House/Outdoor: ").lower()
#         if party_type=="house":
#             print("Go to house party.")
#         elif party_type=="outdoor":
#             print("Go to house outdoor party.")
#         else:
#             print("Enter valid party type House/Outdoor.")
#     elif activity_type=="trip":
#         trip_type=input("Enter trip type Local/Outstation: ").lower()
#         if trip_type=="local":
#             print("Go to local trip.")
#         elif trip_type=="outstation":
#             print("Go to outstation.")
#         else:
#             print("Enter valid trip type Local/Outstation.")
#     elif activity_type=="movie":
#         movie_type=input("Enter movie type Theatre or OTT: ").lower()
#         if movie_type=="theatre":
#             print("Go to theatre.")
#         elif movie_type=="ott":
#             print("Go to ott.")
#         else:
#             print("Enter valid movie type Theatre or OTT.")
#     else:
#         print("Enter valid activity type Party/Trip/movie.")
# else:
#     print("Enter valid day_type weekend/weekday.")

# 10.
# signal_color=input("Enter the colour of the signal : ").lower()
# if signal_colour == "red":
#     print("Stop")
# elif signal_color == "yellow":
#     print("Wait")
# elif signal_color == "green":
#     print("Go")
# else:
#     print("Enter valid signal color red/yellow/green")