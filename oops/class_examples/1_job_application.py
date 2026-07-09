class JobApplication:
    # class variable
    company = "Accenture"

    # constructor
    def __init__(self, candidate_name, job_title,skill):
        self.candidate_name = candidate_name
        self.job_title = job_title
        self.skill = skill
        # print(f"candidate name : {self.candidate_name} \njob title : {self.job_title}")

    # instance method
    def training(self):
        return f"{self.skill} for {self.candidate_name} "

    #  class method
    @classmethod
    def employer(cls):
        return f"Employer is {JobApplication.company}"

    # static method
    # here you are accessing instance variable in static not a good practice
    # @staticmethod
    # def job_description(job):
    #     return f"{job.skill} skill is required"

    @staticmethod
    def eligibility():
        return "Minimum qualification: B.Tech"

    # property
    @property
    def processing(self):
        return "application processed"

    # instance method
    def recruitment(self):

        return (f"Instance variable :You recruited {self.candidate_name} for job {self.job_title}\n"
                f"Instance method   : candidates are getting trained for {self.training()}\n"
                f"Class variable    : company name {JobApplication.company}\n"
                f"Class method      : {JobApplication.employer()}\n"
                # f"Static method     : {JobApplication.job_description(self)}\n"
                f"Static method     : {self.eligibility()}"
                f"Property          : {self.processing}\n")

    def candidate_details(self):
        return (f"Candidate       : {self.candidate_name}\n"
                f"Job title       : {self.job_title}\n"
                # f"Job description : {JobApplication.job_description(self)}\n"
                f"Job description : {self.eligibility()}\n"
                f"Training        : {self.training()}\n"
                f"Employer        : {self.employer()}\n"
                f"Status          : {self.processing} ")



candidate1=JobApplication("Teja","Data engineer","Python")
candidate2=JobApplication("Harsha","Java developer","Java")
# print(detail1.training())
# print(detail2.training())
# print(detail1.candidate_name)
# print(detail1.job_title)
# print(JobApplication.company)
# print(detail1.recruitment())
print("Candidate1 details-->")
print(candidate1.candidate_details())
print("\nCandidate2 details-->")
print(candidate2.candidate_details())