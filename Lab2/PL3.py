#Demonstrate the difference between mutable and immutable data types.
#Create a list and a tuple.Try to modify an element in both the list and the tuple.Observe the results and explain the difference.

mylist = [1, 2, 3, 4, 5]

mytuple = (1, 2, 3, 4, 5)


mylist[0] = 10

mytuple[0] = 10 # This will raise an error

# Print the modified list and tuple
print("Modified list:", mylist)
print("Tuple:", mytuple)