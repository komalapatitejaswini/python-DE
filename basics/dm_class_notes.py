
# money = float(input("enter money: "))
# if money >= 500:
#     print("go to movie")
# else:
#     print("study python")

# wrong output
# money = float(input("enter money: "))
# if money >= 500:
#     print("go to movie")
# elif money >= 1000:
#     print("go to shopping")
# else:
#     print("go to trip")

# correct code that passes all testcases and has single output
# money = float(input("enter money: "))
# if money >= 5000:
#     print("go to trip")
# elif money >= 1000:
#     print("go to shopping")
# elif money >= 500:
#     print("go to movie")
# else:
#     print("study python")

# multiple ifs to print various outputs
# if money >= 5000:
#     print("go to trip")
# if money >= 1000:
#     print("go to shopping")
# if money >= 500:
#     print("go to movie")

# day_type = input("enter day type weekend/weekday: ")
# money = float(input("enter money: "))
#
# if day_type == 'weekend' and money >= 500:
#     print("go to movie")
#
# if day_type == 'weekend' or money >= 500:
#     print("go to movie")


# num = int(input("enter num: "))

# if num > 0:
#     print("positive")
# elif num < 0:
#     print("negative")
# else:
#     print("zero")

# less probable
# if num == 0:
#     print("zero")
# elif num < 0:
#     print("negative")
# else:
#     print("positive")


# marks = int(input("enter marks: "))

# if marks > 100 or marks < 0:
#     print("enter valid marks")
# elif marks >= 75:
#     print("first class")
# elif marks >= 50:
#     print("second class")
# elif marks >= 35:
#     print("just pass")
# else:
#     print("fail")

# if marks >= 75 and marks <= 100:
#     print("first class")
# elif marks >= 50 and marks < 75:
#     print("second class")
# elif marks >= 35 and marks < 50:
#     print("just pass")
# elif marks >= 0 and marks < 35:
#     print("fail")
# else:
#     print("provide valid marks")

# optimized code
# if 75 <= marks <= 100:
#     print("first class")
# elif 50 <= marks < 75:
#     print("second class")
# elif 35 <= marks < 50:
#     print("just pass")
# elif 0 <= marks < 35:
#     print("fail")
# else:
#     print("provide valid marks")

# takes time as checks all conditions even though in 1st if condition is met
# if 0 <= marks <= 100:
#     if 75 <= marks <= 100:
#         print("first class")
#     if 50 <= marks < 75:
#         print("second class")
#     if 35 <= marks < 50:
#         print("just pass")
#     if 0 <= marks < 35:
#         print("fail")
# else:
#     print("provide valid marks")

# day_type = input("enter day type weekday/weekend: ")
#
# if day_type == "weekday":
#     print("go to office")
# elif day_type == "weekend":
#     activity_type = input("enter activity type movie/party/trip: ")
#     if activity_type == "movie":
#         movie_type = input("enter movie type ott/theater: ")
#         if movie_type == 'ott':
#             print("watch movie in ott")
#         elif movie_type == "theater":
#             print("watch movie in theatre")
#         else:
#             print("enter valid movie type")
#     elif activity_type == "party":
#         party_type = input("enter party type house/outside: ")
#         if party_type == "house":
#             print("enjoy house party")
#         elif party_type == "outside":
#             print("enjoy outside party")
#         else:
#             print("enter valid party type house/outside")
#     elif activity_type == "trip":
#         trip_type = input("enter trip type local/outstation: ")
#         if trip_type == "local":
#             print("enjoy local trip")
#         elif trip_type == "outstation":
#             print("enjoy outstation trip")
#         else:
#             print("enter valid trip type local/outstation")
#     else:
#         print("enter valid activity type movie/party/trip")
# else:
#     print("enter valid day type weekday/weekend")

