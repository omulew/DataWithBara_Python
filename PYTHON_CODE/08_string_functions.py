name = "Krystian"
age = 42

# print("Your age is: " + str(age))
# print("Your age is:", str(age))

password = "123a"

# print(len(password))
# if len(password) < 8:
#     print("Password is too short")

text = """
Python is easy to learn.
Python is hard to learn.
Python is powerful.
"""
# print(text.count("Python"))

date = "2026/05/10"
# print(date)
# print(date.replace("/","-"))

price = "1234,56"
# print(price)
# print(price.replace(",","."))

price = "$1,234.56"
# print(price)
# print(price.replace([^0-9],""))

# f-string
# print(f"My name is {name} and i'm {age} years old")
# print(f"2 + 3 = {2 + 3}")
# print(f"{{2 + 3}} = {2 + 3}")

# split()
text = "Ada-24-USA"
# print(text.split("-"))

text = "2026-09-20"
# print(text.split("-"))

# print("ha" * 3) #hahaha

#       654321
text = "Python"
#       012345
# print(text[0])
# print(text[-6])
# print(text[0:3])
# print(text[0:5:2])
# print(text[-6:3])

text = " Krys tian Przybył ek "
# print(f"\"{text.lstrip()}\"")
# print(f"\"{text.rstrip()}\"")
# print(f"\"{text.strip()}\"")
# print(f"\"{text.strip(" K")}\"")

text = " Krystian PRZYBYŁek"
# print(text)
# print(text.lower())

text = "2026-Feb-10"
# print(text.startswith("2026"))
# print(text.endswith("2026"))
# print(text.find("2026"))
# print("02" in text)

text = "USA"
print(text.isalpha())
print(text.isnumeric())
