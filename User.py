# your User class goes here
class User:

    def __init__(self, first_name = "", last_name = "", email_address = "", license_number = ""):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.license_number = license_number

    def get_user_input(self):
        self.first_name = input("Enter your first name: ")
        print(f'First name is confirmed as: {self.first_name}.')
        self.last_name = input("Enter your last name: ")
        print(f'Last name is confirmed as: {self.last_name}.')
        self.email_address = input("Enter your email address: ")
        print(f'Email address is confirmed as: {self.email_address}.')
        self.license_number = input("Enter your driver's license number: ")
        print(f"Driver's license is confirmed as: {self.license_number}.")

    def __str__(self):
        return f"You have chosen a user. That user's information is: \n First Name: {self.first_name} \n Last Name: {self.last_name} \n Email address: {self.email_address} \n Driver's License: {self.license_number}."
        # return f"You have chosen a user. That user's information is: \n First Name: {self.first_name} \n Last Name: {self.last_name} \n"
        # return (
        #     f"You have chosen {self.first_name} {self.last_name}. \n"
        # )
        

user1 = User() # define the variable as the whole class.

user1.get_user_input() # call the user variable, but then chain the get_user_input method onto it. 
# self.give_user_info(self)
print(user1)
