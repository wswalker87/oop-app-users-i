# import User
from User import Users, FreeUser, PremiumUser

# free_user = Users.create_new_user(FreeUser)

# premium_user =  PremiumUser("Someone_Cool", "steal@thisemail.com")
# premium_user = Users.create_new_user(PremiumUser)


# --- Creating Users ---
print("\n--- Creating Premium User (user_A@example.com) ---")
# Calling create_new_user and passing the PremiumUser class as the argument
premium_user_A = Users.create_new_user(PremiumUser) 

print("\n--- Creating Free User (user_B@example.com) ---")
# Calling create_new_user and passing the FreeUser class as the argument
free_user_B = Users.create_new_user(FreeUser)

# --- Testing FreeUser Post Limit ---
print("\n--- Testing FreeUser Post Limit ---")
free_user_B.add_post() # 1st Post
free_user_B.add_post() # 2nd Post
free_user_B.add_post() # 3rd Post (Should print the limit message)

# --- Testing PremiumUser Posts ---
print("\n--- Testing PremiumUser Posts ---")
premium_user_A.add_post()
premium_user_A.add_post()
premium_user_A.add_post()

# --- Final Check ---
print("\n--- Final User State ---")
print(premium_user_A)
print(free_user_B)
