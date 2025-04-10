# Program 23
# Write a Python Program to Find HCF.
import math

def hcf(number1,number2):
    return math.gcd(number1,number2)
number1=int(input("Enter your number : "))
number2=int(input("Enter your number : "))

result=hcf(number1,number2)
print(result)


# Python program to find H.C.F of two numbers
# define a function
def compute_hcf(x, y):
# choose the smaller number
 if x > y:
    smaller = y
 else:
    smaller = x
 for i in range(1, smaller+1):
    if((x % i == 0) and (y % i == 0)):
        hcf = i
 return hcf
num1 = int(input('Enter the number: '))
num2 = int(input('Enter the number: '))
print("The H.C.F. is", compute_hcf(num1, num2))


# Program 24
# Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal.

def decimal_to_binary(num):
    return bin(num).replace("0b", "")
def decimal_to_octal(num):
    return oct(num).replace("0o", "")
def decimal_to_hexadecimal(num):
    return hex(num).replace("0x", "")

number=int(input("Enter your number : "))
print(decimal_to_binary(number))
print(decimal_to_octal(number))
print(decimal_to_hexadecimal(number))


def converter_bin_oct_hex(number):
   print(bin(number))
   print(oct(number))
   print(hex(number))

   
number=int(input("Enter your number : "))
converter_bin_oct_hex(number)


# Program 25
# Write a Python Program To Find ASCII value of a character.

print(ord("4"))


# Program 26
# Write a Python Program to Make a Simple Calculator with 4 basic mathematical
# operations.


# This function adds two numbers
def add(x, y):
 return x + y
def subtract(x, y):
 return x - y

def multiply(x, y):
 return x * y
# This function divides two numbers
def divide(x, y):
 return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
 # take input from the user
 choice = input("Enter choice(1/2/3/4): ")
 # check if choice is one of the four options
 if choice in ('1', '2', '3', '4'):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
 if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))
 elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))
 elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))
 elif choice == '4':
        print(num1, "/", num2, "=", divide(num1, num2))
 next_calculation = input("Let's do next calculation? (yes/no):")
 if next_calculation == "no":
    break
 else:
    print("Invalid Input")
