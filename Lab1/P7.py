#Manipulate strings using various built-in functions.
#o Create a string variable and find the length of the string.
#o Convert the string to uppercase and lowercase.
#o Check if a substring exists in the string.
#o Split the string into a list of words.

# Create a string variable
my_string = "Hello, World!"

# Find the length of the string
length = len(my_string)
print("Length of the string:", length)

# Convert the string to uppercase
uppercase_string = my_string.upper()
print("Uppercase string:", uppercase_string)

# Convert the string to lowercase
lowercase_string = my_string.lower()
print("Lowercase string:", lowercase_string)

# Check if a substring exists in the string
substring = "Hello"
if substring in my_string:
    print("Substring exists in the string")
else:
    print("Substring does not exist in the string")

# Split the string into a list of words
word_list = my_string.split()
print("List of words:", word_list)
