#Create a program to print the multiplication table of a number.Take a number as input from the user.Use a for loop to iterate from 1 to 10.Calculate the product of the input number and the current iteration.Print the multiplication table.
num = int(input("Enter a number: "))

for i in range(1, 11):
    product = num * i
    print(num, "x", i, "=", product)