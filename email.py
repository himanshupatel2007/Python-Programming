email = input("Enter your Email : ")
if email.count("@") :
    index = email.index("@")
    user_name = email[:index]
    domain = email[index+1 :]
    print(f"Your user name : {user_name} and Domain : {domain}")
else : print("Enter a valid Email")