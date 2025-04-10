# Program 21
# Write a Python Program to Find the Sum of Natural Numbers.

start_number=int(input("Enter start number : "))
end_number=int(input("Enter end number : "))
if start_number%2==0 and not start_number==1:
   print("invalid number")
sum=0
for i in range(start_number,end_number,2):
    sum=sum+i
print(sum)

limit = int(input("Enter the limit: "))
# Initialize the sum
sum = 0
# Use a for loop to calculate the sum of natural numbers
for i in range(1, limit + 1):
 sum += i
# Print the sum
print("The sum of natural numbers up to", limit, "is:", sum)


# Program 21
# Write a Python Program to Find the Sum of Natural Numbers.


start_number=int(input("Enter your start number : "))
end_number=int(input("Enter your end number : "))

sum=0
for i in range(start_number,end_number):
   sum+=i
print(f"Sum of all natutal number is : {sum}")

   
# Program 22
# Write a Python Program to Find LCM

# Formula:

            # LCM(𝑎, 𝑏) =|𝑎 ⋅ 𝑏|/GCD(𝑎, 𝑏)



def LCM(a,b):
   if a>b:
      grater=a
   else:
      grater=b
   while(True):
      if((grater % a == 0) and (grater % b == 0)):
         lcm=grater
         break
      grater+=1
   return lcm
num1 = int(input('Enter the number: '))
num2 = int(input('Enter the number: '))

our_lcm=LCM(num1,num2)
print(our_lcm)

def gcd(a,b):
   while b:
      a,b=b,a%b
   return a
def lcm(a,b):
   return abs(a*b)

num1=int(input("Enter number first : "))
num2=int(input("Enter number second : "))

result=lcm(num1,num2)
print(result)

import math
def lcm(a,b):
   return abs(a*b)//math.gcd(a,b)

num1=int(input("Enter number first : "))
num2=int(input("Enter number second : "))

result=lcm(num1,num2)
print(result)

def lcm(numbe1,number2):
   return abs(numbe1*number2)//math.gcd(numbe1,number2)

num1=int(input("Enter number first : "))
num2=int(input("Enter number second : "))

result=lcm(num1,num2)
print(result)
