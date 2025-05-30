# Prompt the user to enter a number and convert the input to an integer
User = int(input("Enter a number: "))

# Check if the entered number is divisible by 2 (even number)
if User % 2 == 0:
    # If the number is even, print that it is an even number
    print(User, "is an even number.")

else:
    # If the number is not even (odd), print that it is an odd number
    print(User, "is an odd number.")