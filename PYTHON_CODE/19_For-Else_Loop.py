# x = [1, 2, 3, 4]
# for i in x:
#     print(i)
# else:
#     print("End loop")


# items = [1, 3, 5]
# for i in items:
#     if i % 2 == 0:
#         print(f"Even Nr. Found: \"{i}\"")
#         break
# else:
#     print("All numbers are odd")


names = ['Kamara', 'Tuba', '', 'Monica']
for name in names:
    if name is None or name == '':
        print(f"Founding a missing name: \"{name}\"")
        break
else:
    print("All names are available")
