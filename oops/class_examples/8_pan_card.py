class PANCard:

    department = "Income Tax Department"

    def __init__(self, applicant, city):
        self.applicant = applicant
        self.city = city

    def verify_aadhaar(self):
        return "Aadhaar Verified"

    @classmethod
    def authority(cls):
        return cls.department

    @staticmethod
    def processing_days():
        return "15 days"

    @property
    def pan_status(self):
        return "PAN Generated"

    def pan_details(self):
        return (
            f"Applicant       : {self.applicant}\n"
            f"City            : {self.city}\n"
            f"verification    : {self.verify_aadhaar()}\n"
            f"Authority       : {self.authority()}\n"
            f"Processing Time : {self.processing_days()}\n"
            f"Status          : {self.pan_status}"
        )


pan1 = PANCard("Tejaswini", "Anantapur")

print(pan1.applicant)
print(pan1.city)
print(pan1.pan_details())
