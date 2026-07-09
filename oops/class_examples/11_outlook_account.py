class OutlookAccount:

    company = "Microsoft"

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def create_user(self):
        return f"{self.email} got Created"

    @classmethod
    def company_name(cls):
        return cls.company

    @staticmethod
    def password_rules():
        return "Password must contain 8 characters"

    @property
    def account_status(self):
        return "Account Activated"

    def account_details(self):
        return (
            f"Username : {self.username}\n"
            f"Email    : {self.email}\n"
            f"Account  : {self.create_user()}\n"
            f"company  : {self.company_name()}\n"
            f"Password : {self.password_rules()}\n"
            f"Status   : {self.account_status}"
        )


outlook1 = OutlookAccount("teja_544", "tejaswini@outlook.com")
print(outlook1.username)
print(outlook1.email)
print(outlook1.account_details())
