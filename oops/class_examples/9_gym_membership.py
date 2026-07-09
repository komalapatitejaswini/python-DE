class GymMembership:

    gym = "STONES Gym"

    def __init__(self, member_name, plan):
        self.member_name = member_name
        self.plan = plan

    def allocate_trainer(self):
        return "Trainer Assigned"

    @classmethod
    def gym_name(cls):
        return cls.gym

    @staticmethod
    def working_hours():
        return "Open 5 AM to 10 PM"

    @property
    def membership_status(self):
        return "Membership Active"

    def membership_details(self):
        return (
            f"Member      : {self.member_name}\n"
            f"Plan        : {self.plan}\n"
            f"Trainer     : {self.allocate_trainer()}\n"
            f"Gym name    : {self.gym_name()}\n"
            f"Gym timings : {self.working_hours()}\n"
            f"Status      : {self.membership_status}"
        )
member1 = GymMembership("Tejaswini", "Annual Plan")

print(member1.member_name)
print(member1.plan)
print(member1.membership_details())
