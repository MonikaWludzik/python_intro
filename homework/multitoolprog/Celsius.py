def interger_check(prompt):
    value = input(prompt)
    while value.isnumeric() is False:
        value = input("Please provide a number ")
    return int(float(value))


def Ceslius():
    Celsius = interger_check("Temperature in Celsius ")
    print("T(°F) = T(°C) × 9/5 + 32")
    print(Celsius)
    print(f"{Celsius} x 9/5 + 32")
    print(round(Celsius * (9 / 5) + 32))