#zadanie 5
#calculating dog's age

# we want the user to enter an integer.
# we want to keep asking them until they give us an integer.
# we will store their integer in this variable.
# we set it to false to start, because false is not a number. because it is not a number, it means the while loop will happen.
# the while loop will keep hapenning
dog_age = ""
while dog_age.isnumeric() is False:
    dog_age = input("Insert dog's age: ")

print((((int(dog_age)-2)*4)+21))