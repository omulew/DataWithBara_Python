# 1 Python Challenge
# Validate the Quality and Correctness of Email Values (Walidacja jakości i poprawności wartości e-mail)
# Zasady walidacji:
#     Must not be empty (Nie może być pusty)
#     Must contain '.' and '@' (Musi zawierać kropkę '.' oraz symbol '@')
#     Must contain exactly one '@' symbol (Musi zawierać dokładnie jeden symbol '@')
#     Must end with '.com', '.org', or '.net' (Musi kończyć się rozszerzeniem '.com', '.org' lub '.net')
#     Must not be longer than 254 characters (Nie może być dłuższy niż 254 znaki)
#     Must start and end with a letter or digit (Musi zaczynać się i kończyć literą lub cyfrą)

email = "test@gmail.com"

email = email.strip()

if email is None or email == '':
    print(f"Email must not be empty, email = '{email}'")
elif not ('@' in email and '.' in email):
    print(f"Email must contain '.' and '@', email = '{email}'")
elif email.count("@") != 1:
    print(f"Email must contain exactly one '@' symbol, email = '{email}'")
elif email.endswith(('.com', '.org', '.net')) == False:
    print(f"Email must end with '.com', '.org', or '.net', email = '{email}'")
elif len(email) > 254:
    print(f"Email must not be longer than 254 characters, email = '{email}'")
elif not (email[0].isalnum() and email[-1].isalnum()):
    print(
        f"Email must start and end with a letter or digit, email = '{email}'")
else:
    print(f"Email is OK, email = '{email}'")
