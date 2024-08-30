#Create a program to find the sum of all even numbers between 1 and 100
def sum():
    total = 0
    for number in range(0,101):
        total += number
    return total

# Example usage:
result = sum()
print("The sum of all even numbers between 1 and 100 is: ",result )