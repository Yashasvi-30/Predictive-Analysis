#Create and access tuples	Create a tuple of colors.	Access elements using indexing.	Try to modify an element in the tuple (to demonstrate immutability).Find the number of occurrences of a specific element in the tuple.

colors = ("red", "green", "blue", "yellow","red","yellow","red","purple")


first_color = colors[0]
second_color = colors[1]
last_color = colors[-1]


colors[0] = "orange"


count_red = colors.count("red")
count_green = colors.count("green")
count_blue = colors.count("blue")
count_yellow = colors.count("yellow")
