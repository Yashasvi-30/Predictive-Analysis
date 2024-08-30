#Create a program to find the factorial of a number using a loop and conditional statements

def factorial(n):
    result = 1
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0:
        return 1
    else:
        for i in range(1, n+1):
            result *= i
        return result

number = int(input("Enter a number: "))
fact = factorial(number)
print("The factorial of", number, "is", fact)