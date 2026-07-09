# # 1.Job application
# print("1.Job application")
# full_name=input("Enter your full name:")
# contact_number=input("Enter your contact number:")
# location=input("Enter your location:")
# highest_qualification=input("Enter your highest qualification:")
# skills=[str(x) for x in input("Enter your skills:").split()]
# hasexperience=input("Do you have experience?Enter yes or no:").strip().lower()
# print(hasexperience=="yes")
# years=int(input("Enter years of experience:"))
# months=int(input("Enter months of experience:"))
# experience={"years":years,"months":months}
# print(full_name,contact_number,location,highest_qualification,skills,hasexperience,f"your experience is {experience['years']} years and {experience['months']} months")
# print(f"your experience is {experience['years']} years and {experience['months']} months")
# print(type(full_name),type(contact_number),type(location),type(highest_qualification),type(skills),type(experience),type(hasexperience))
#
# # 2.Insta account creation
# print("2.Insta account creation")
# phone_number=input("Enter your phone number:")
# email=input("Enter your email:")
# full_name=input("Enter your full name:")
# username=input("Enter your username:")
# dob=input("Enter your dob:")
# print(phone_number,email,full_name,username,dob)
# print(type(phone_number),type(email),type(full_name),type(username),type(dob))
#
# # 3.Outlook account creation
# print("3.Outlook account creation")
# desired_email_address=input("Enter your desired email address:")
# password=input("Enter your password:")
# first_name=input("Enter your first name:")
# last_name=input("Enter your last name:")
# country=input("Enter your country:")
# dob=input("Enter your dob:")
# print(desired_email_address,first_name,last_name,country,dob)
# print(type(desired_email_address),type(first_name),type(last_name),type(country),type(dob))
#
# # 4.Movie ticket booking
# print("4.Movie ticket booking")
# location=input("Enter your location:")
# movie_name=input("Enter your movie name:")
# theater=input("Enter your theater:")
# show_time=input("Enter your show time:")
# seat_number=int(input("Enter your seat number:"))
# print(location,movie_name,theater,show_time,seat_number)
# print((type(location),type(movie_name),type(theater),type(show_time),type(seat_number)))
#
# # 5.Gym membership
# print("5.Gym membership")
# name=input("Enter your name:")
# age=int(input("Enter your age:"))
# height=float(input("Enter your height:"))
# weight=float(input("Enter your weight:"))
# plan=input("Enter your plan:")
# print(name,age,height,weight,plan)
# print(type(name),type(age),type(height),type(weight),type(plan))
#
# # 6.Apply for pan card
# print("6.Apply for pan card")
# full_name=input("Enter your full name:")
# father_name=input("Enter your father name:")
# dob=input("Enter your dob:")
# gender=input("Enter your gender:")
# contact_info=input("Enter your contact info:")
# residential_address=input("Enter your residential address:")
# aadhaar_number=input("Enter your aadhar number:")
# print(full_name,father_name,dob,gender,contact_info,residential_address,aadhaar_number)
# print(type(full_name),type(father_name),type(dob),type(gender),type(contact_info),type(residential_address),type(aadhaar_number))
#
# # 7.Ordering food online
# print("7.Ordering food online")
# delivery_address=input("Enter your delivery address:")
# contact_number=input("Enter your contact number:")
# dish=input("Enter your dish:")
# payment_method=input("Enter your payment method:")
# print(delivery_address,contact_number,dish,payment_method)
# print((type(delivery_address),type(contact_number),type(dish),type(payment_method)))
#
# # 8.Booking bus ticket  
# print("8.Booking bus ticket")
# origin=input("Enter your origin:")
# destination=input("Enter your destination:")
# date_of_journey=input("Enter your date of journey:")
# seat_number=int(input("Enter your seat number:"))
# passenger_details=input("Enter your passenger details:")
# print(origin,destination,date_of_journey,seat_number,passenger_details)
# print(type(origin),type(destination),type(date_of_journey),type(passenger_details))
#
# # 9.Applying loan
# print("9.Applying loan")
# basic_details=[str(x) for x in input("Enter your basic details:").split()]
# contact_details=[str(x) for x in input("Enter your contact details:").split()]
# id_card=input("Enter your id card:")
# loan_amount=float(input("Enter your loan amount:"))
# credit_score=int(input("Enter your credit score:"))
# print(f"My basic details are {basic_details}")
# print(contact_details)
# print(id_card)
# print(loan_amount)
# print(credit_score)
# print((type(basic_details),type(contact_details),type(id_card),type(loan_amount),type(credit_score)))
#
# # 10.Applying for health insurance
# print("10.Applying for health insurance")
# basic_details=[str(x) for x in input("Enter your basic details:").split()]
# print(basic_details)
# for ele in basic_details:
#     print(ele)
# contact_details=[str(x) for x in input("Enter your contact details:").split()]
# family_details=[str(x) for x in input("Enter your family details:").split()]
# pre_existing_conditions=[str(x) for x in input("Enter your preexisting conditions:").split()]
# past_surgeries=[str(x) for x in input("Enter your past surgeries:").split()]
# id_proof=input("Enter your id proof:")
# print(basic_details,contact_details,family_details,pre_existing_conditions,past_surgeries,id_proof)
# print((type(basic_details)),(type(contact_details)),(type(family_details)),(type(pre_existing_conditions)),(type(past_surgeries)),(type(id_proof)))