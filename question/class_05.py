# Program 11
# Write a Python Program to Check if a Number is Positive, Negative or Zero

number=int(input("Enter your value that check : "))

def check_number(number):
    if number >=1:
        return "Positive number"
    elif number == 0:
        return "Zero number"
    else:
        return "Negative number"
    
ch_number=check_number(number)
print(ch_number)


num = int(input("Enter a number: "))
if num > 0:
 print("Positive number")
elif num == 0:
 print("Zero")
else:
 print("Negative number")


# Program 12
# Write a Python Program to Check if a Number is Odd or Even.

number=int(input("Enter your number that check for even and odd : "))
def checknumber(number):
   if number%2==0:
      return f"Your number is even :{number}"
   else:
      return f"Your number is odd :{number}"
   
check_number=checknumber(number)
print(check_number)
    
num = int(input("Enter a number: "))
if num%2 == 0:
 print("This is a even number")
else:
 print("This is a odd number")


# Program 13
# Write a Python Program to Check Leap Year

year=int(input("Enter your year that check leap year : "))

def leep_year(year):
   if year%4==0 and year%100==0 and year%400==0:
      return f"This is leap year : {year}"
   else:
      return f"This is not leap year : {year}"
    
enter_year=leep_year(year)
print(enter_year)


year = int(input("Enter a year: "))
# divided by 100 means century year (ending with 00)
# century year divided by 400 is leap year
if (year % 400 == 0) and (year % 100 == 0):
 print("{0} is a leap year".format(year))
# not divided by 100 means not a century year
# year divided by 4 is a leap year
elif (year % 4 ==0) and (year % 100 != 0):
 print("{0} is a leap year".format(year))
# if not divided by both 400 (century year) and 4 (not century year)
# year is not leap year
else:
 print("{0} is not a leap year".format(year))
