"""
Day 9 - Temperature Converter
"""


def celcius_to_fahreinheit(x):
    return (x * 9 / 5) + 32


def celcius_to_kelvin(x):
    return x + 273.15


def fahreinheit_to_celcius(x):
    return (x - 32) * 5 / 9


def fahreinheit_to_kelvin(x):
    return (x - 32) * 5 / 9 + 273.15


def kelvin_to_celcius(x):
    return x - 273.15


def kelvin_to_fahreinheit(x):
    return (x - 273.15) * 9 / 5 + 32


def main():
    unit = str(input("Enter temperature unit (c/f/k): "))
    num = int(input("Enter temperature value: "))
    to = str(input("Convert temperature to (c/f/k): "))

    if unit == "c" and to == "f":
        print(f"{num} Celcius is", celcius_to_fahreinheit(num), "Fahreinheit")
    elif unit == "c" and to == "k":
        print(f"{num} Celcius is", celcius_to_kelvin(num), "Kelvin")
    elif unit == "f" and to == "c":
        print(f"{num} Fahreinheit is", fahreinheit_to_celcius(num), "Celcius")
    elif unit == "f" and to == "k":
        print(f"{num} Fahreinheit is", fahreinheit_to_kelvin(num), "Kelvin")
    elif unit == "k" and to == "c":
        print(f"{num} Kelvin is", kelvin_to_celcius(num), "Celcius")
    elif unit == "k" and to == "f":
        print(f"{num} Kelvin is", kelvin_to_fahreinheit(num), "Fahreinheit")
    else:
        print("Invalid value!")


if __name__ == "__main__":
    main()
