print("Enter the details for the AP series:")
first = int(input("What is the first term (a)? "))
difference = int(input("What is the common difference (d)? "))
n = int(input("Which term do you want to find (n)? "))
nth = first + (n - 1) * difference
sum = (n / 2) * (2 * first + (n - 1) * difference)
print(f"The {n}th term in your series is: {nth}")
print(f"The sum of the series up to the {n}th term is: {sum}")
