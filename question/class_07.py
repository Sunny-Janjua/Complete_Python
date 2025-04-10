# Program 16
# Write a Python Program to Find the Factorial of a Number.

fact_number=int(input("Enter your number that take factorial : "))

def factorial(fact_number):
    fact=1
    if fact_number<=1:
      return "Invalid number!"
    for i in range(1,fact_number+1):
        fact=fact*i
    return fact
factorail_num=factorial(fact_number)
print(factorail_num)


num = int(input("Enter a number: "))
factorial = 1
if num <0:
 print("Factirial does not exist for negative numbers")
elif num == 0:
 print("Factorial of 0 is 1")
else:
 for i in range(1, num+1):
    factorial = factorial*i
 print(f'The factorial of {num} is {factorial}')



# Program 17
# Write a Python Program to Display the multiplication Table.
table=int(input("Enter your number that take table : "))
for i in range(1,11):
  print(f"{table} * {i} = {table*i}")

num = int(input("Display multiplication table of: "))
for i in range(1, 11):
 print(f"{num} X {i} = {num*i}")





