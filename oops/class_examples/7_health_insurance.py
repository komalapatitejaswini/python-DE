class HealthInsurance:

    company = "Star Health"

    def __init__(self, customer_name, policy):
        self.customer_name = customer_name
        self.policy = policy

    def verify_medical_history(self):
        return "Medical History Verified"

    @classmethod
    def insurance_company(cls):
        return cls.company

    @staticmethod
    def waiting_period():
        return "30 days"

    @property
    def policy_status(self):
        return "Policy Activated"

    def insurance_details(self):
        return (
            f"Customer       : {self.customer_name}\n"
            f"Policy         : {self.policy}\n"
            f"verification   : {self.verify_medical_history()}\n"
            f"Company        : {self.insurance_company()}\n"
            f"Waiting Period : {self.waiting_period()}\n"
            f"Status         : {self.policy_status}"
        )
insurance1 = HealthInsurance("Tejaswini", "Family Health Plan")

print(insurance1.customer_name)
print(insurance1.policy)
print(insurance1.insurance_details())
