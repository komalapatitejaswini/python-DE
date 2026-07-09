# # 1.Job Application
#
# class JobApplication:
#     # class variable
#     company = "Accenture"
#
#     # constructor
#     def __init__(self, candidate_name, job_title):
#         self.candidate_name = candidate_name
#         self.job_title = job_title
#         print(f"candidate name : {self.candidate_name} \njob title : {self.job_title}")
#
#     # instance method
#     def training(self):
#         return f"DE for {self.candidate_name} "
#
#     #  class method
#     @classmethod
#     def employer(cls):
#         return f"Employer is {JobApplication.company}"
#
#     # static method
#     @staticmethod
#     def job_description():
#         return "Python skill is required"
#
#     # property
#     @property
#     def processing(self):
#         return "application processed"
#
#     # instance method
#     def recruitment(self):
#
#         return (f"Instance variable :You recruited {self.candidate_name} for job {self.job_title}\n"
#                 f"Instance method : candidates are getting trained for {self.training()}\n"
#                 f"Class variable : company name {JobApplication.company}\n"
#                 f"Class method : {JobApplication.employer()}\n"
#                 f"Static method : {self.job_description()}\n"
#                 f"Property : {self.processing}\n")
#
#
# detail1=JobApplication("Teja","Associate_engineer")
# print(detail1.candidate_name)
# print(detail1.job_title)
# print(JobApplication.company)
# print(detail1.job_description())
#
# # 2.Bank Account creation
#
# class BankAccount:
#
#     bank_name="HDFC"
#     ifsc_code="HDFC001"
#
#     def __init__(self, customer_name,account_number,balance):
#         self.name = customer_name
#         self.account_number = account_number
#         self.balance = balance
#
#     # @balance.setter
#     # def balance(self, value):
#     #     self._balance = value
#
#     def deposit(self, amount):
#         self.balance += amount
#
#     def withdraw(self, amount):
#         self.balance -= amount
#
#     def account_details(self):
#         return (f"Customer Name   : {self.name}\n"
#                 f"Bank name       : {BankAccount.bank_name}\n"
#                 f"Account number  : {self.account_number}\n"
#               # f"Balance after deposit: {self.deposit(100000)}"
#               # f"Balance after withdrawal: {self.withdraw(1000)}"
#                 f"Balance         : {self.balance}\n"
#                 f"{self.account_creation()}")
#
#     @classmethod
#     def bank_details(cls):
#         return f"Bank name : {cls.bank_name}\nIFSC code :  {cls.ifsc_code}"
#
#     @staticmethod
#     def account_creation():
#         return "Account created successfully"
#
#
# account1=BankAccount("Teja",123456,10000000)
# account2=BankAccount("ram",234567,20000000)
# print("Account1 details-->")
# account1.deposit(100000)
# account1.withdraw(1000)
# print(account1.account_details())
# print("\nAccount2 details-->")
# print(account2.account_details())
# print("\nBank details-->")
# print(BankAccount.bank_details())
#
#
# # 3.Instagram Account creation
#
# class InstagramAccount:
#
#     platform = "Instagram"
#
#     def __init__(self, username, email):
#         self.username = username
#         self.email = email
#
#     def create_profile(self):
#         return f"{self.username}'s profile is created"
#
#     @classmethod
#     def company_name(cls):
#         return f"Platform : {cls.platform}"
#
#     @staticmethod
#     def account_rules():
#         return "Username must be unique"
#
#     @property
#     def status(self):
#         return "Account Created Successfully"
#
#     def account_details(self):
#         return (
#             f"Username : {self.username}\n"
#             f"Email : {self.email}\n"
#             f"Instance Method : {self.create_profile()}\n"
#             f"Class Method : {self.company_name()}\n"
#             f"Static Method : {self.account_rules()}\n"
#             f"Property : {self.status}"
#         )
#
# insta1 = InstagramAccount("tejaswini_123", "teja@gmail.com")
#
# print(insta1.username)
# print(insta1.email)
# print(insta1.account_details())
#
#
# # 4.Food Order
#
# class FoodOrder:
#
#     restaurant = "Domino's"
#
#     def __init__(self, customer_name, food_item):
#         self.customer_name = customer_name
#         self.food_item = food_item
#
#     def place_order(self):
#         return f"{self.food_item} ordered"
#
#     @classmethod
#     def restaurant_name(cls):
#         return cls.restaurant
#
#     @staticmethod
#     def delivery_time():
#         return "Delivery in 30 minutes"
#
#     @property
#     def order_status(self):
#         return "Order Confirmed"
#
#     def order_details(self):
#         return (
#             f"Customer : {self.customer_name}\n"
#             f"Food : {self.food_item}\n"
#             f"{self.place_order()}\n"
#             f"Restaurant : {self.restaurant_name()}\n"
#             f"{self.delivery_time()}\n"
#             f"Status : {self.order_status}"
#         )
#
# order1 = FoodOrder("Tejaswini", "Veg Pizza")
#
# print(order1.customer_name)
# print(order1.food_item)
# print(order1.order_details())
#
#
#
# # 5.Bus ticket Booking
#
# class BusBooking:
#
#     company = "APSRTC"
#
#     def __init__(self, passenger, destination):
#         self.passenger = passenger
#         self.destination = destination
#
#     def reserve_seat(self):
#         return "Seat Reserved"
#
#     @classmethod
#     def transport(cls):
#         return cls.company
#
#     @staticmethod
#     def luggage_policy():
#         return "20 kg luggage allowed"
#
#     @property
#     def ticket_status(self):
#         return "Ticket Booked"
#
#     def booking_details(self):
#         return (
#             f"Passenger : {self.passenger}\n"
#             f"Destination : {self.destination}\n"
#             f"{self.reserve_seat()}\n"
#             f"Company : {self.transport()}\n"
#             f"{self.luggage_policy()}\n"
#             f"Status : {self.ticket_status}"
#         )
#
# ticket1 = BusBooking("Tejaswini", "Bangalore")
#
# print(ticket1.passenger)
# print(ticket1.destination)
# print(ticket1.booking_details())
#
#
# # 6.Loan Application
#
# class LoanApplication:
#
#     bank = "HDFC"
#
#     def __init__(self, customer_name, loan_amount):
#         self.customer_name = customer_name
#         self.loan_amount = loan_amount
#
#     def verify_documents(self):
#         return "Documents Verified"
#
#     @classmethod
#     def bank_name(cls):
#         return cls.bank
#
#     @staticmethod
#     def interest_rate():
#         return "Interest Rate : 9%"
#
#     @property
#     def loan_status(self):
#         return "Loan Approved"
#
#     def application_details(self):
#         return (
#             f"Customer : {self.customer_name}\n"
#             f"Loan Amount : {self.loan_amount}\n"
#             f"{self.verify_documents()}\n"
#             f"Bank : {self.bank_name()}\n"
#             f"{self.interest_rate()}\n"
#             f"Status : {self.loan_status}"
#         )
#
# loan1 = LoanApplication("Tejaswini", 500000)
#
# print(loan1.customer_name)
# print(loan1.loan_amount)
# print(loan1.application_details())
#
#
# # 7.Health Insurance
#
# class HealthInsurance:
#
#     company = "Star Health"
#
#     def __init__(self, customer_name, policy):
#         self.customer_name = customer_name
#         self.policy = policy
#
#     def verify_medical_history(self):
#         return "Medical History Verified"
#
#     @classmethod
#     def insurance_company(cls):
#         return cls.company
#
#     @staticmethod
#     def waiting_period():
#         return "Waiting Period : 30 days"
#
#     @property
#     def policy_status(self):
#         return "Policy Activated"
#
#     def insurance_details(self):
#         return (
#             f"Customer : {self.customer_name}\n"
#             f"Policy : {self.policy}\n"
#             f"{self.verify_medical_history()}\n"
#             f"Company : {self.insurance_company()}\n"
#             f"{self.waiting_period()}\n"
#             f"Status : {self.policy_status}"
#         )
# insurance1 = HealthInsurance("Tejaswini", "Family Health Plan")
#
# print(insurance1.customer_name)
# print(insurance1.policy)
# print(insurance1.insurance_details())
#
#
#
# # 8.PAN Card creation
#
# class PANCard:
#
#     department = "Income Tax Department"
#
#     def __init__(self, applicant, city):
#         self.applicant = applicant
#         self.city = city
#
#     def verify_aadhaar(self):
#         return "Aadhaar Verified"
#
#     @classmethod
#     def authority(cls):
#         return cls.department
#
#     @staticmethod
#     def processing_days():
#         return "Processing Time : 15 days"
#
#     @property
#     def pan_status(self):
#         return "PAN Generated"
#
#     def pan_details(self):
#         return (
#             f"Applicant : {self.applicant}\n"
#             f"City : {self.city}\n"
#             f"{self.verify_aadhaar()}\n"
#             f"{self.authority()}\n"
#             f"{self.processing_days()}\n"
#             f"Status : {self.pan_status}"
#         )
#
#
# pan1 = PANCard("Tejaswini", "Anantapur")
#
# print(pan1.applicant)
# print(pan1.city)
# print(pan1.pan_details())
#
#
# # 9.Gym Membership
#
# class GymMembership:
#
#     gym = "Gold's Gym"
#
#     def __init__(self, member_name, plan):
#         self.member_name = member_name
#         self.plan = plan
#
#     def allocate_trainer(self):
#         return "Trainer Assigned"
#
#     @classmethod
#     def gym_name(cls):
#         return cls.gym
#
#     @staticmethod
#     def working_hours():
#         return "Open 5 AM to 10 PM"
#
#     @property
#     def membership_status(self):
#         return "Membership Active"
#
#     def membership_details(self):
#         return (
#             f"Member : {self.member_name}\n"
#             f"Plan : {self.plan}\n"
#             f"{self.allocate_trainer()}\n"
#             f"{self.gym_name()}\n"
#             f"{self.working_hours()}\n"
#             f"Status : {self.membership_status}"
#         )
# member1 = GymMembership("Tejaswini", "Annual Plan")
#
# print(member1.member_name)
# print(member1.plan)
# print(member1.membership_details())
#
#
#
# # 10.Movie Ticket Booking
#
# class MovieBooking:
#
#     theatre = "PVR Cinemas"
#
#     def __init__(self, customer_name, movie):
#         self.customer_name = customer_name
#         self.movie = movie
#
#     def reserve_seat(self):
#         return "Seat Reserved"
#
#     @classmethod
#     def theatre_name(cls):
#         return cls.theatre
#
#     @staticmethod
#     def cancellation():
#         return "Cancellation allowed before 2 hours"
#
#     @property
#     def booking_status(self):
#         return "Ticket Confirmed"
#
#     def booking_details(self):
#         return (
#             f"Customer : {self.customer_name}\n"
#             f"Movie : {self.movie}\n"
#             f"{self.reserve_seat()}\n"
#             f"{self.theatre_name()}\n"
#             f"{self.cancellation()}\n"
#             f"Status : {self.booking_status}"
#         )
#
# movie1 = MovieBooking("Tejaswini", "Kalki 2898 AD")
#
# print(movie1.customer_name)
# print(movie1.movie)
# print(movie1.booking_details())
#
#
#
# # 11.Outlook Account creation
#
# class OutlookAccount:
#
#     company = "Microsoft"
#
#     def __init__(self, username, email):
#         self.username = username
#         self.email = email
#
#     def create_mailbox(self):
#         return "Mailbox Created"
#
#     @classmethod
#     def company_name(cls):
#         return cls.company
#
#     @staticmethod
#     def password_rules():
#         return "Password must contain 8 characters"
#
#     @property
#     def account_status(self):
#         return "Account Activated"
#
#     def account_details(self):
#         return (
#             f"Username : {self.username}\n"
#             f"Email : {self.email}\n"
#             f"{self.create_mailbox()}\n"
#             f"{self.company_name()}\n"
#             f"{self.password_rules()}\n"
#             f"Status : {self.account_status}"
#         )
#
#
# outlook1 = OutlookAccount("tejaswini", "tejaswini@outlook.com")
# print(outlook1.username)
# print(outlook1.email)
# print(outlook1.account_details())
#
