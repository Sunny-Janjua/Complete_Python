# Program 14
# Write a Python Program to Check Prime Number

num = int(input("Enter a number: "))
flag = False
if num == 1:
    print(f"{num}, is not a prime number")
elif num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True 
            break

if flag:
 print(f"{num}, is not a prime number")
else:
 print(f"{num}, is a prime number")


def is_prime(num):
   if num<=1:
      return False
   for i in range(2,num):
      if num%i==0:
         return False
      return True
num=int(input("Enter your number : "))
if is_prime(num):
   print("Prime number")
else:
   print("Not prime number")
   


def prime_number(number):
   if num<=1:
      return False
   for i in range(2,number):
      if number%i==0:
         return False 
      return True
number=int(input("Enter your number : "))
if prime_number(number):
   print("Prime number")
else:
   print("not prime number")


# Program 15 ¶
# Write a Python Program to Print all Prime Numbers in an Interval of 1-10.


start_number=int(input("Enter start number : "))
end_number=int(input("Enter end number : "))

for num in range(start_number,end_number+1):
   if num>1:
      for i in range(2,num):
         if num%i==0:
            break
      else:
         print(num)

lower = 1
upper = 10
print("Prime numbers between", lower, "and", upper, "are:")
for num in range(lower, upper + 1):
 # all prime numbers are greater than 1
 if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            break
    else:
        print(num)
