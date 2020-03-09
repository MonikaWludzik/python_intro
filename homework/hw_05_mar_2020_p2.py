#zadanie 5
#print(num1/num2/num3/num4)

height1 = input("Input the length of the top and the bottom edge of the rectangle: ")
width1 = input("Input the length of the left and right edge of the rectangle: ")
height2 = (int(height1)*("-"))
print(height2)

width2 = (int(width1)*"|")
row = str(width2[0] + int(height1)*' ' + width2[1])
print(row + '\n')











