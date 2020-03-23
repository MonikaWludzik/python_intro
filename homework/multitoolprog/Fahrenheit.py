def intergercheck(prompt):
    value = input(prompt)
    while value.isnumeric() is False:
        value = input("Please provide a number ")
    return int(float(value))

def Fahrenheit():
    Fahrenheit = intergercheck("Temperature in Fahrenheit ")
    print("T(°C) = (T(°F) - 32) × 5/9")
    print(Fahrenheit)
    print(f"{Fahrenheit} - 32) × 5/9)")
    print(round((Fahrenheit-32)*(5/9)))