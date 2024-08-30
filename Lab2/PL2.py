#Create and manipulate dictionaries.
#Create a dictionary to store information about a person (name, age, city).
#Access values using keys.
#Add a new key-value pair to the dictionary.
#Modify an existing value.
#Check if a key exists in the dictionary.
#Get a list of all keys and values.


person = {
    "name": "Yashasvi Gupta",
    "age": 21,
    "city": "Lucknow"
}


name = person["name"]
age = person["age"]
city = person["city"]
print("Name:", name)
print("Age:", age)
print("City:", city)


person["occupation"] = "Student"

print("Occupation:", person["occupation"])

person["age"] = 30


if "name" in person:
    print("Name exists in the dictionary.")


keys = person.keys()
values = person.values()

print("Keys:", keys)
print("Values:", values)
