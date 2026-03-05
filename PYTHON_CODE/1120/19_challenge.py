file_list = [
    'raport.csv',
    'data.xlsx',
    'summary.docx',
    'raport.csv',
    'data.csv'
]

for file in file_list:
    if file_list.count(file) > 1:
        print(f"Founding duplicate file: \"{file}\"")
        break
else:
    print("NO duplicates")
