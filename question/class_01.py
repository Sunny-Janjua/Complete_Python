# Program 1
# Write a Python program to print Hello Python

print("Hello Python")

# Program 2
# Write a Python program to do arithmetical operations addition and division.



def addition(number1,number2):
    return number1+number2
def subtraction(number1,number2):
    return number1-number2
def multiplaction(number1,number2):
    return number1*number2
def division(number1,number2):
    return number1/number2
def modulus(number1,number2):
    return number1%number2
def floor_division(number1,number2):
    return number1//number2
def power(number1,number2):
    return number1**number2

number1=int(input("Enter your first number for input : "))
number2=int(input("Enter your second number for input : "))
print("-"*30)
print("Well Come to my Calculator!")
print("-"*30)
print("01_For Addition")
print("02_For Multiplication")
print("03_For Division")
print("04_For Subtraction")
print("05_For Modulus")
print("06_For Floor Division")
print("07_For Power")
print("08_For End Cal!")
print("-"*30)


while(True):
    choices=input("Enter your choices : ")
    try:
        match choices:
            case "1":
                print(addition(number1,number2))
            case "2":
                print(multiplaction(number1,number2))
            case "3":
                print(division(number1,number2))
            case "4":
                print(subtraction(number1,number2))
            case "5":
                print(modulus(number1,number2))
            case "6":
                print(floor_division(number1,number2))
            case "7":
                print(power(number1,number2))
            case "8":
                break
    except Exception as e:
        print(str(e))




