#zadanie 6
#binary numbers

numbertoconvert = input("Provide a six digit binary number: ")
decimal_num = int(numbertoconvert, 2)
print(decimal_num)

#Zadanie 7
#odd numbers

n = int(input("Provide any number: "))
if(n%2==0) :
    print("This an even number")
else :
    print("This an odd number")

#Zadanie 8

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

div = int(input("Provide any number: "))
if div%3==0 and div%5==0 and div%7==0 :
    print("The number can be divided by 3, 5 and 7")
else:
    print("The number cannot be divided by 3,5, and 7")

#Zadanie 10

#est podzielny przez 4, ale nie jest podzielny przez 100
#jest podzielny przez 400

year = int(input("Provide any year: "))
if year%4==0 and year%100!=0:
    print("This is a leap year")
if year%400==0:
    print("This is a leap year")
elif year%4!=0 or year%100!=0 or year%400!=0 :
    print("This is not a leap year")


