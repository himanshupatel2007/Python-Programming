print("Please enter three numbers to find the maximum.")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
bigger = num1 if num1 > num2 else num2
max= bigger if bigger > num3 else num3
print(f"The maximum of {num1}, {num2}, and {num3} is: {max}")
