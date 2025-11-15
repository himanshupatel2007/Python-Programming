name = input("Enter your name:")
is_valid = name.replace(" ", "").isalpha()
if is_valid:
    print(f"Hello, {name}!")
else:
    print("Invalid name. Please use alphabetic characters only.")