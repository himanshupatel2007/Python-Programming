password = input("Enter your name:")
is_valid = password.count(" ") 
valid = password.isalpha()
if is_valid and valid:
    print(f"Hello, {password}!")
else:
    print("Invalid name. Please use alphabetic characters only.")