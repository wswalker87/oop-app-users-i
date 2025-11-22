from abc import ABC, abstractmethod
# your User class goes here
class Users:

    all_users = {}

    def __init__(self, first_name = "", last_name = "", email_address = "", license_number = "", post  = ""):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.license_number = license_number
        self.post = post
        if self.email_address != "":
            self.add_user_to_all_users()

    def add_user_to_all_users(self):
        """Adds this instance's details to the class attribute, all_users."""
        # Access the class attribute via the class name
        Users.all_users[self.email_address] = self # add to all_users using email address


    def create_new_user(self):
        first_name = input("Enter your first name: ")
        print(f'First name is confirmed as: {first_name}.')
        last_name = input("Enter your last name: ")
        print(f'Last name is confirmed as: {last_name}.')
        email_address = input("Enter your email address: ")
        print(f'Email address is confirmed as: {email_address}. This will be your username')
        license_number = input("Enter your driver's license number: ")
        print(f"Driver's license is confirmed as: {license_number}. We don't know why we need it. We might sell it.")

        new_user = Users(first_name, last_name, email_address, license_number)
        if email_address not in Users.all_users:
            print(f'Successfully addes new user. ')

    def add_post(self):
        # which post?
        user_posts = input("Enter your post here: ")
        self.post = user_posts
        print(f"Post has been posted: {user_posts}")
        #take post?
    
        

    def __str__(self):
        return f"You have chosen a user. That user's information is: \n First Name: {self.first_name} \n Last Name: {self.last_name} \n Email address: {self.email_address} \n Driver's License: {self.license_number}. {self.all_users}"
        # return f"You have chosen a user. That user's information is: \n First Name: {self.first_name} \n Last Name: {self.last_name} \n"
        # return (
        #     f"You have chosen {self.first_name} {self.last_name}. \n"
        # )
        

user1 = Users() # define the variable as the whole class.

user1.create_new_user() # call the user variable, but then chain the get_user_input method onto it. 
# self.give_user_info(self)
print(user1)
