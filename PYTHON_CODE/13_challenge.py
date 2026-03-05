user_name = "Krystian"
age = 42
password = "  "
email = "krystian@test.com"
user_role = "admin"  # moderator
is_banned = False
is_email_verified = True

# 1
# print(f"User's name '{user_name}' is not empty: {bool(user_name)}")
# print(f"User's age '{age}' is greater than or equal to 18: {age >= 18}")

# 2
# print(
#     f"Password characters '{password}' is at least 8 char.: {len(password) >= 8 and " " in password}")

# 3
# print(
# f"User's email '{email}' is not empty, contains '@', and ends with '.com': {len(email) > 0 and "@" in email and email.endswith(".com")}")
# print(f"Users'email is empty: {not bool(email)}")
# print(f"Users'email is empty: {not bool(email)}")

# 4
print(
    f"User's name '{user_name}'is a string: {isinstance(user_name, str)}, is not None: {not (user_name is not None)}, and is longer than 5 characters: {
        (user_name is str or user_name is None) and len(user_name) > 5}")

# 5
