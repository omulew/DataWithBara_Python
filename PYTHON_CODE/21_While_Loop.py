
# i = 0
# while i < 4:
#     print(f"Value of i = \"{i}\"")
#     i += 1


# while True:
#     answer = input("Do you agree? (yes/no): ")
#     if answer == "yes":
#         break
# print("Thank you!")

# number_of_answers = 0
# while True:
#     answer = input("Do you agree? (yes/no): ")
#     number_of_answers += 1
#     if answer == "yes":
#         print("Glad we are on the same page.")
#         break
#     elif number_of_answers == 3:
#         print("3 Strikes, You are out")
#         break
# print("Thank you!")


# number_of_answers = 0
# while number_of_answers < 3:
#     answer = input("Do you agree? (yes/no): ")
#     if answer == "yes":
#         print("Glad we are on the same page.")
#         break
#     elif number_of_answers == 3:
#         print("3 Strikes, You are out")
#         break
#     number_of_answers += 1
# print("Thank you!")


number_of_answers = 0
while number_of_answers < 3:
    answer = input("Do you agree? (yes/no): ")
    if answer == "yes":
        print("Glad we are on the same page.")
        break
    number_of_answers += 1
else:
    print("3 Strikes, You are out")

print("Thank you!")
