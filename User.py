# your User class goes here
class User:

    def __init__(self, first_name, last_name, email_address, license_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.license_number = license_number

    def user_input(self):
        first_name = input("Enter your first name: ")
        print(f'First name is confirmed as: {first_name}.')
        last_name = input("Enter your last name: ")
        print(f'Last name is confirmed as: {last_name}.')
        email_address = input("Enter your email address: ")
        print(f'Confirmed')