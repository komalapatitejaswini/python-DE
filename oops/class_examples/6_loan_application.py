class LoanApplication:

    bank = "HDFC"

    def __init__(self, customer_name, loan_amount,doc_name):
        self.customer_name = customer_name
        self.loan_amount = loan_amount
        self.doc_name = doc_name

    def verify_documents(self):
        return f"{self.doc_name} Verified"

    @classmethod
    def bank_name(cls):
        return cls.bank

    @staticmethod
    def interest_rate():
        return "Interest Rate : 9%"

    @property
    def loan_status(self):
        return "Loan Approved"

    def application_details(self):
        return (
            f"Customer    : {self.customer_name}\n"
            f"Loan Amount : {self.loan_amount}\n"
            f"Documents   : {self.verify_documents()}\n"
            f"Bank        : {self.bank_name()}\n"
            f"ROI         : {self.interest_rate()}\n"
            f"Status      : {self.loan_status}"
        )

loan1 = LoanApplication("Tejaswini", 500000, "PAN-Card")

print(loan1.customer_name)
print(loan1.loan_amount)
print(loan1.application_details())
