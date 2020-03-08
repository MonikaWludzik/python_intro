#Zadanie 1 i 2
#T(°F) = T(°C) × 9/5 + 32
#T(°C) = (T(°F) - 32) × 5/9

Fahrenheit = input("Temperature in Fahrenheit ")
temp1 = int(Fahrenheit)
print("T(°C) = (T(°F) - 32) × 5/9")
print(Fahrenheit)
print("({} - 32) × 5/9".format(temp1))
print(round((temp1-32)*(5/9)))

Celsius = input("Temperature in Celsius ")
temp2 =int(Celsius)
print("T(°F) = T(°C) × 9/5 + 32")
print(Celsius)
print("{} x 9/5 + 32".format(temp2))
print(round((temp2)*(9/5)+32))

#Zadanie 3
#P = 3,14159 • r2

Area = input("Area of a circle calculation, press enter to continue")
radius = input("Input the circle's radius in centimetres ")
rad = float(radius)
print("formula = 3,14159 • r2")
area = (round(pow(rad,rad)*(3.14159)))
print("{} cm".format(area))

#Zadanie 4

yournumber = input("Input your number ")
ynumber = str(yournumber)
print(ynumber[0])
print(ynumber[-1])