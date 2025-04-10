# Program 8
# Write a Python program to display calendar.

import calendar

year=int(input("Enter your year : "))
month=int(input("Enter your month : "))

print_value=calendar.month(year,month)
print(print_value)


year = int(input("Enter year: "))
month = int(input("Enter month: "))
cal = calendar.month(year, month)
print(cal)

year=int(input("Enter your year : "))
def complete_year(year):
    return (calendar.calendar(year))

com_year=complete_year(year)
print(f"This is our complete year : {com_year}")

# Program 10
# Write a Python program to swap two variables without temp variable.

a = 5
b = 10
# Swapping without a temporary variable
a, b = b, a
print("After swapping:")
print("a =", a)
print("b =", b)

