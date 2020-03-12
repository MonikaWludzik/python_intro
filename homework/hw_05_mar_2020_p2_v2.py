#zadanie 5
#print(num1/num2/num3/num4)

bottom1 = int(input("Input the length of the top and the bottom edge of the rectangle: "))
side1 = int(input("Input the length of the left and right edge of the rectangle: "))
bottom2 = (int(bottom1)*("-"))
print("+" + bottom2 + "+")

whitespace = " " * bottom1
side2 = "|" + (" "*(bottom1)) + "|\n"
side2 = f"|{whitespace}|\n"
print(side2*bottom1, end='')
print("+" + bottom2 + "+")


#row = str(width2[0] + int(height1)*' ' + width2[1])
#print (row)
#"+" + (" ")
#"|"
#4 * ("|" + )
#print (automatycznie dodaje znak nowej linii
#print(row + '\n')






