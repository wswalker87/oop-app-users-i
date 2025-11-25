from abc import ABC, abstractmethod
# your User class goes here


class Users(ABC):
    @abstractmethod
    def make_the_squiggle_go_away(self): # after adding the @abstract decorator, it wanted a function directly after, so the dicts below it were throwing an error
        return

    all_users = {}
    all_posts = {}

    def __init__(self, first_name = "", last_name = "", email_address = "", license_number = ""):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.license_number = license_number
        self.posts = []
        if self.email_address != "":
            self.add_user_to_all_users()

    def add_user_to_all_users(self):
        """Adds this instance's details to the class attribute, all_users."""
        # Access the class attribute via the class name
        Users.all_users[self.email_address] = self # add to all_users using email address

    @staticmethod
    def create_new_user(UserClass):
        """Create a new user and return it"""
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        email_address = input("Enter your email address: ")
        license_number = input("Enter your driver's license number: ")

        new_user = UserClass(first_name, last_name, email_address, license_number)
        print(f"\nSuccessfully added user: {new_user.email_address}")
        return new_user # I was missing the actual return of the obj
        # if email_address not in Users.all_users:
        #     print(f'Successfully addes new user. ')

    def add_post(self):
        # which post?
        user_posts = input("Enter your post here: ")
        # self.post = user_posts # need to use append like the one below. else it just overwrites the list
        self.posts.append(user_posts)
        print(f"Post has been posted: '{user_posts}'")

    def delete_post(self):
        if not self.posts: # if there is nothing in self.posts
            print("No posts.")
            return
        print("\nYour current posts are: ")
        
        for i, post in enumerate(self.posts):
            print(f"[{i}]: {post[:50]}...") # if the post is super long, shorten it to the first 50 charactersCalled truncating

        try: #try, but throw error if no valid inxed 
            index_to_delete = int(input("FInd the post you want and enter the index here: "))

            if 0 <= index_to_delete < len(self.posts): # if user chose index greater than of eq to 0 and less than the number of posts total
                deleted_post = self.posts.pop(index_to_delete)
                print(f"Post deleted successfully: '{deleted_post[:30]}...'")
            else:
                print("Invalid index") # less than 0 or greater than the length of thte dict
        except ValueError:
            print("Invalid input. You have to use a number.")

    def __str__(self):
        return (f"User: {self.first_name} {self.last_name} {self.email_address}\nNumber of posts: {len(self.posts)} total.")
        #  return f"You have chosen a user. That user's information is: \n First Name: {self.first_name} \n Last Name: {self.last_name} \n Email address: {self.email_address} \n Driver's License: {self.license_number}. {self.all_users}"
        # return f"You have chosen a user. That user's information is: \n First Name: {self.first_name} \n Last Name: {self.last_name} \n"
        # return (
        #     f"You have chosen {self.first_name} {self.last_name}. \n"
        # )
"""Req:
    - User class needs to be a base class (from abc import ABC, abstractmethod)
    - Two new classes, PremiumUser and FreeUser, that inherit from Users
    - Overrid the add_post() for FreeUser so that an instance of FreeUser is limited to two posts
    - In the runner file, import FreeUser and PremiumUser and create at least one instance of each
    - Add testing """

class PremiumUser(Users):
    def __init__(self, first_name="", last_name="", email_address="", license_number=""):
        super().__init__(first_name, last_name, email_address, license_number)

    def make_the_squiggle_go_away(self): # after adding the @abstract decorator, it wanted a function directly after, so the dicts below it were throwing an error
        return


class FreeUser(Users):
    def __init__(self, first_name="", last_name="", email_address="", license_number=""):
        super().__init__(first_name, last_name, email_address, license_number)

    def make_the_squiggle_go_away(self): # after adding the @abstract decorator, it wanted a function directly after, so the dicts below it were throwing an error
        return


    def add_post(self): # This method inherits from FreeUser, which in turn inherits from Users. It then overwrites the add_post method from the User Class
        # check how many posts. Free only gets 2 posts
        # set number of posts to equal the length of a 
        number_of_posts = len(self.posts)
        if number_of_posts  >= 2:
            print("You've reached the max number of posts for a free user.")
            return
        user_posts = input("Enter your post here: ")
        # self.post = user_posts # need to use append like the one below. else it just overwrites the list
        self.posts.append(user_posts)
        print(f"Post has been posted: '{user_posts}'")
        

print("--- Creating User ---")
user1 = Users.create_new_user(PremiumUser)
user1 = Users.create_new_user(FreeUser)

print("\n--- Adding Posts ---")
user1.add_post() 
user1.add_post() 


print("\n--- Deleting a Post ---")
user1.delete_post()

print("\n--- Final Check ---")
print(user1)
