
person = ['Maria', 29, 'Data Engineer', 'Spain']
name, age, role, country = person

# print(f"name: {name}")
# print(f"age: {age}")
# print(f"role: {role}")
# print(f"country: {country}")

person = ['Maria', 29, 'Data Engineer', 'Spain']
name, *details, country = person

# print(f"name: {name}")
# print(f"details: {details}")
# print(f"country: {country}")

person = ['Maria', 29, 'Data Engineer', 'Spain']
name, _, _, country = person

# print(f"name: {name}")
# print(f"country: {country}")


person = ['Maria', 29, 'Data Engineer', 'Spain']
name, *_, country = person

print(f"name: {name}")
print(f"country: {country}")
