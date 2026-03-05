# 🚀 #2 Python Challenge**
# Validate the Quality and Correctness of Passwords**


email = "test@tesrkacz.com"
password = "df3TR8!#$15"

# Must not be empty**
if password is None or password == '':
    print(f"password must not be empty, password = '{password}'")
# Must be at least 8 characters**
elif len(password) <= 8:
    print(
        f"password must be longer than 8 characters, password = '{password}'")
# Must include at least 1 uppercase**
elif password.isupper():
    print(
        f"password must include at least 1 uppercase, password = '{password}'")
# Must include at least 1 lowercase**
elif password.islower():
    print(
        f"password must include at least 1 lowercase, password = '{password}'")
# Must not be same as the email**
elif password == email:
    print(
        f"password must not be same as the email, password = '{password}'")
# Must not contain any spaces**
elif password.count(" ") != 0:
    print(
        f"password must not contain any spaces, password = '{password}'")
# Must start and end with a letter or digit**
elif not (password[0].isalnum() and password[-1].isalnum()):
    print(
        f"password must start and end with a letter or digit, password = '{password}'")
else:
    print(f"password is OK, password = '{password}'")
