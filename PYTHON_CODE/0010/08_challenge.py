text = "968-Maria, ( D@t@ Engineer ) ;; 27y  "
print(f"\"{text}\"")

text = text.strip().replace("@", "a")
print(f"\"{text}\"")
print(
    f"\"name: {text[4:9].lower()} | role: {text[13:26].lower()} | age: {text[-3:-1]}\"")
