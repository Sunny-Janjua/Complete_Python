# Program 27
# Write a Python Program to Display Fibonacci Sequence Using Recursion.

def fab(number):
    if number<=1:
        return number
    else:
        return (fab(number-1)+(fab(number-2)))
    
number=int(input("Enter your number tha take fab : "))

for i in range(number):
    print(fab(i))


# Python program to display the Fibonacci sequence
def recur_fibo(n):
 if n <= 1:
    return n
 else:
    return(recur_fibo(n-1) + recur_fibo(n-2))
nterms = int(input("Enter the number of terms (greater than 0): "))
# check if the number of terms is valid
if nterms <= 0:
 print("Plese enter a positive integer")
else:
 print("Fibonacci sequence:")
 for i in range(nterms):
    print(recur_fibo(i))


# Program 28
# Write a Python Program to Find Factorial of Number Using Recursion.

def fact(number):
   if number<=1:
      return 1
   else:
      return number*fact(number-1)
number=int(input("Enter your number : "))
factorial=fact(number)
print(factorial)

# Factorial of a number using recursion
def recur_factorial(n):
 if n == 1:
    return n
 else:
    return n*recur_factorial(n-1)
num = int(input("Enter the number: "))
# check if the number is negative
if num < 0:
 print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
 print("The factorial of 0 is 1")
else:
 print("The factorial of", num, "is", recur_factorial(num))


# Program 29
# Write a Python Program to calculate your Body Mass Index.

def BMI(weight,height):
  return (weight//height)

weight=int(input("Enter your value : "))
height=int(input("Enter your value : "))

bmi=BMI(weight,height)
print(f"Your BMI is : {bmi}")


def bodymassindex(height, weight):
 return round((weight / height**2),2)
h = float(input("Enter your height in meters: "))
w = float(input("Enter your weight in kg: "))
print("Welcome to the BMI calculator.")
bmi = bodymassindex(h, w)
print("Your BMI is: ", bmi)
if bmi <= 18.5:
 print("You are underweight.")
elif 18.5 < bmi <= 24.9:
 print("Your weight is normal.")
elif 25 < bmi <= 29.29:
 print("You are overweight.")
else:
 print("You are obese.")


# Program 30
# Write a Python Program to calculate the natural logarithm of any number.

import math
num = float(input("Enter a number: "))
if num <= 0:
 print("Please enter a positive number.")
else:
 # Calculate the natural logarithm (base e) of the number
 result = math.log(num)
 print(f"The natural logarithm of {num} is: {result}")


# Program 31
# Write a Python Program for cube sum of first n natural numbers?
cube_sum=0
num = int(input("Enter the value of n: "))
for i in range(1,num+1):
  cube_sum+=i*i*i
print(cube_sum)


def cube_sum_of_natural_numbers(n):
 if n <= 0:
    return 0
 else:
    total = sum([i**3 for i in range(1, n + 1)])
 return total
# Input the number of natural numbers
n = int(input("Enter the value of n: "))
if n <= 0:
 print("Please enter a positive integer.")
else:
 result = cube_sum_of_natural_numbers(n)
 print(f"The cube sum of the first {n} natural numbers is: {result}")