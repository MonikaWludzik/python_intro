def piramida():

    num1 = input('Fill in your favourite number from 1 to 100: ')
    while num1.isnumeric() is False:
        num1 = input("Please provide a number ")
    result = int(num1)


    def pyramid(num):
        for row in range(1, num + 1):
            spacing = ' ' * (num - row)
            print(spacing + ('#' * (2 * row - 1)))

    pyramid(result)
