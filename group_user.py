# your User class goes here
class User:
    all_users = []
    def __init__(self, user_name = "", user_post):
        self.user_name = user_name
        self.user_post = user_post
    
    
    def add_user(self):
        user_name = input("Enter your username: ")
        user_post = input("Enter your post here: ")
        new_user = User(user_name, user_post = [])
        if user_name not in self.all_users:
            new_user += self.all_users
            print('User added.')
        else:
            print('Username not available.')
user1 = User()
user1.add_user()
print(user1)