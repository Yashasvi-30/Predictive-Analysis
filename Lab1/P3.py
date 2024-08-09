# Write a program to take user input, process it, and display the result.
#Prompt the user to enter their name.
#Greet the user using their name.
#Calculate and print the user's age based on their birth year.

name = input("Enter your name: ")   
print("Hello", name)
birth_year = int(input("Enter your birth year: "))
age = 2024 - birth_year
print("Your age is: ", age)
