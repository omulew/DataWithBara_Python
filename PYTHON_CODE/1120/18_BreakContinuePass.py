# names = ["john", "maria", '', "kumar"]

# for name in names:
#     if name == '':
#         print("Empty value detected!")
#         break
#     print(f"Name = \"{name}\"")

# names = ["john", "maria", '', "kumar"]
# for name in names:
#     if name == '':
#         print("Empty value detected!")
#         continue
#     print(f"Name = \"{name}\"")


# names = ["john", "maria", '', "kumar"]
# for name in names:
#     if name == '':
#         # print("Empty value detected!")
#         # pass    # todo: Handle Empty Value
#         name = name.replace('', 'unknown')
#     print(f"Name = \"{name}\"")

days = ['Mon', 'Sun', 'Wed', 'Tue', 'Sut']
weekends = ['Sun', 'Sut']
for day in days:
    if day in weekends:
        print(f"Weekend day = \"{day}\"")
        continue
    print(f"Working day = \"{day}\"")
