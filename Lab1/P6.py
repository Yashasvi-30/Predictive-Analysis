#Create a list, access elements, modify elements, and perform list operations.
#o Create a list of fruits.
#o Access elements using indexing.
#o Modify elements in the list.
#o Add and remove elements from the list.
#o Find the length of the list.
#o Sort the list in ascending and descending order.

fruits = ['Litchi', 'Banana', 'Mango', 'Cherry']

# Accessing elements using indexing
print(fruits[0])  
print(fruits[2])  

# Modifying elements in the list
fruits[1] = 'grape'
print(fruits)  

# Adding elements to the list
fruits.append('orange')
print(fruits)  

# Removing elements from the list
fruits.remove('Cherry')
print(fruits)  

# Finding the length of the list
print(len(fruits))  

# Sorting the list in ascending and descending order
fruits.sort()
print(fruits)  

fruits.sort(reverse=True)
print(fruits)  
