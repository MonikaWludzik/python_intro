
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
