class InstagramAccount:

    platform = "Instagram"

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def create_profile(self):
        return f"{self.username}'s profile is created"

    @classmethod
    def company_name(cls):
        return f"Platform : {cls.platform}"

    @staticmethod
    def account_rules():
        return "Username must be unique"

    @property
    def status(self):
        return "Account Created Successfully"

    def account_details(self):
        return (
            f"Username        : {self.username}\n"
            f"Email           : {self.email}\n"
            f"Instance Method : {self.create_profile()}\n"
            f"Class Method    : {self.company_name()}\n"
            f"Static Method   : {self.account_rules()}\n"
            f"Property        : {self.status}"
        )

user1 = InstagramAccount("tejaswini_544", "teja@gmail.com")
user2 = InstagramAccount("harsha_44", "harsha@gmail.com")

print(user1.username)
print(user1.email)
print("\nuser1 details-->")
print(user1.account_details())
print("\nuser2 details-->")
print(user2.account_details())
