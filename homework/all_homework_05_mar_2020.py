#Zadanie 1

def intergercheck(prompt):
    value = input(prompt)
    while value.isnumeric() is False:
        value = input("Please provide a number ")
    return int(float(value))

Fahrenheit = intergercheck("Temperature in Fahrenheit ")

print("T(°C) = (T(°F) - 32) × 5/9")
print(Fahrenheit)
print(f"{Fahrenheit} - 32) × 5/9)")
print(round((Fahrenheit-32)*(5/9)))

#Zadanie 2

Celsius = intergercheck("Temperature in Celsius ")

print("T(°F) = T(°C) × 9/5 + 32")
print(Celsius)
print(f"{Celsius} x 9/5 + 32")
print(round(Celsius * (9 / 5) + 32))

#Zadanie 3


def input_float(prompt):
    value = False
    isAFloat = False
    while isAFloat is False:
              #input("Input the circle's radius in centimetres: ")
        value = input(prompt)
        try:
            value = float(value)
            isAFloat = True
        except:
            print("Please provide a decimal number ")
            isAFloat = False

    return (value)


value = input_float("Input the circle's radius in centimetres ")

print("formula = 3,14159 • r2")
area = (round(pow(value,value)*(3.14159)))
print(f"{area} cm")

#Zadanie 4

yournumber = input("Input your number ")
while yournumber.isnumeric() is False:
    yournumber = input("Please provide a number ")
ynumber = str(yournumber)
print(ynumber[0])
print(ynumber[-1])

#Zadanie 5

def draw_square():

    bottom1 = input("Input the length of the top and the bottom edge of the rectangle: ")
    while bottom1.isnumeric() is False:
        bottom1 = input('Please provide a number ')

    side1 = input("Input the length of the left and right edge of the rectangle: ")
    while side1.isnumeric() is False:
        side1 = input("Please provide a number ")

    bottom1 = int(bottom1)
    side1 = int(side1)
    bottom2 = (int(bottom1)*("-"))
    print("+" + bottom2 + "+")

    whitespace = " " * bottom1
    side1 = "|" + (" "*(bottom1)) + "|\n"
    side1 = f"|{whitespace}|\n"
    print(side1*bottom1, end='')
    print("+" + bottom2 + "+")

#Zadanie 6
#binary numbers
#unfinished, needs more blocks

numbertoconvert = input("Provide a six digit binary number: ")
while numbertoconvert.isnumeric() is False:
        numbertoconvert = input("Provide a six digit binary number: ")
decimal_num = int(numbertoconvert, 2)
print(decimal_num)


#Zadanie 7
#odd numbers
#unfinished, needs more blocks

n = int(input("Provide any number: "))
if(n%2==0) :
    print("This an even number")
else :
    print("This an odd number")

#Zadanie 8
#unfinished, needs more blocks

div = int(input("Provide any number: "))
if div%3==0 :
    print("The number can be divided by 3")
if div%5==0 :
    print("The number can be divided by 5")
if div%7==0 :
    print("The number can be divided by 7")
elif div%3!=0 and div%5!=0 and div%7!=0:
    print("The number cannot be divided by 3,5, or 7")

#Zadanie 9
#unfinished, needs more blocks

div = int(input("Provide any number: "))
if div%3==0 and div%5==0 and div%7==0 :
    print("The number can be divided by 3, 5 and 7")
else:
    print("The number cannot be divided by 3,5, and 7")

#Zadanie 10

#unfinished, needs more blocks
#est podzielny przez 4, ale nie jest podzielny przez 100
#jest podzielny przez 400

year = int(input("Provide any year: "))
if year%4==0 and year%100!=0:
    print("This is a leap year")
if year%400==0:
    print("This is a leap year")
elif year%4!=0 or year%100!=0 or year%400!=0 :
    print("This is not a leap year")

