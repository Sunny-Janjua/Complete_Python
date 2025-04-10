# Program 5
# Write a Python program to generate a random number.

import random

value=random.randint(1,10)
print(f"Random values is :{value}")
print(f"Random number: {random.randint(1, 100)}")

# Program 6
# Write a Python program to convert kilometers to miles.

kilometer=int(input("Enter your kilomether that convert into meter : "))
def convert(kilometer):
    conversion_factor = 0.621371
    miles=conversion_factor*kilometer
    return miles
kilomether_convert=convert(kilometer)
print(f"{kilomether_convert} kilometers is equal to miles")
print()


kilometers = float(input("Enter distance in kilometers: "))
# Conversion factor: 1 kilometer = 0.621371 miles
conversion_factor = 0.621371
miles = kilometers * conversion_factor
print(f"{kilometers} kilometers is equal to {miles} miles")


# Program 7
# Write a Python program to convert Celsius to Fahrenheit.

celsius=int(input("Enter your temp : "))
def fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
convert=fahrenheit(celsius)
print(f"Converter : {convert}")

fahrenheit=int(input("Enter your temp : "))
def celsius(fahrenheit):
    celsius = (fahrenheit * 9/5) - 32
    return celsius
convert=celsius(fahrenheit)
print(f"Converter : {convert}")


celsius = float(input("Enter temperature in Celsius: "))
# Conversion formula: Fahrenheit = (Celsius * 9/5) + 32
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees")



