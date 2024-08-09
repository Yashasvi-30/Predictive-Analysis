#Write a Python program to perform basic arithmetic operations (addition, subtraction,
#multiplication, division, and modulus) on two numbers.

num1= int(input("Enter the first number: "))
num2= int(input("Enter the second number: "))


print("Basic Arithmetic operations")

while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exit")
    choice= int(input("Enter your choice: "))

    if choice==1:
        print("Addition of two numbers is: ", num1+num2)
    elif choice==2:
        print("Subtraction of two numbers is: ", num1-num2)
    elif choice==3:
        print("Multiplication of two numbers is: ", num1*num2)
    elif choice==4:
        print("Division of two numbers is: ", num1/num2)
    elif choice==5:
        print("Modulus of two numbers is: ", num1%num2)
    elif choice==6:
        break
    else:
        print("Invalid choice")
        
