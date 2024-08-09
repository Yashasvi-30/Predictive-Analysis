#Write a program to check if a number is even or odd.
#o Prompt the user to enter a number.
#o Use the modulus operator to determine if the number is even or odd.
#o Print the appropriate message.


# Prompt the user to enter a number
number = int(input("Enter a number: "))

# Use the modulus operator to determine if the number is even or odd
if number % 2 == 0:
    print("Number is even.")
else:
    print("Number is odd.")
