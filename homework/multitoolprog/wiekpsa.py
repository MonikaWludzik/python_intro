def wiekpsa():
    dog_age = ""
    while dog_age.isnumeric() is False:
            dog_age = input("Insert dog's age: ")
    print((((int(dog_age)-2)*4)+21))