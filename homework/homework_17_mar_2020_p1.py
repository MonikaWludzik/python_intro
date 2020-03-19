#Zadanie 4

num1 = input('Fill in your favourite number from 1 to 100: ')
result = int(num1)


def pyramid(num):
    for row in range(1, num + 1):
        spacing = ' ' * (num - row)
        print(spacing + ('#' * (2*row-1)))


pyramid(result)


# version rjust
# def pyramid(num):
#     for row in range(1, num + 1):
#         result2 = int(num+row)
#         print(('#' * (2*row-1)).rjust(result2,'.'))
#
#
# pyramid(result)