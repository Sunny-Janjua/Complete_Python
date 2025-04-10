# Program 18
# Write a Python Program to Print the Fibonacci sequence.


def fibonacci_sequence(number):
    if number<=1:
        return number
    if number==2:
        return 1
    else:
        return (fibonacci_sequence(number-1)+fibonacci_sequence(number-2))

number=int(input("Enter number : "))
for i in range(number):
    print(fibonacci_sequence(i))


def fiboacci(num):
 if num <= 1:
    return num
 if num == 2:
    return 1
 else:
    return(fiboacci(num-1) + fiboacci(num-2))
nums = int(input("How many fibonacci numbers you want to generate -"))
for i in range(nums):
 print(fiboacci(i)) # Generate Fibonacci series



nterms = int(input("How many terms? "))
n1, n2 = 0, 1
count = 0
if nterms <= 0:
 print("Please enter a positive integer")
elif nterms == 1:
 print("Fibonacci sequence upto",nterms,":")
 print(n1)
else:
 print("Fibonacci sequence:")
 while count < nterms:
    print(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1

# Program 19
# Write a Python Program to Check Armstrong Number?

def Armstrong(number):
   number_str=str(number)
   number_digit=len(number_str)
   sum_of_powers=sum(int(digit)**number_digit for digit in number_str)
   if sum_of_powers==number:
      return True
   else:
      False

number=int(input("Enter your number that check armstrong : "))
if Armstrong(number):
   print("number is Armstrong")
else:
   print('number is not Armstrong')



# def armstrong(number):
#    numberstr=str(number)
#    numberdigit=len(numberstr)
#    sumnew=0
#    for i in numberdigit:
#       sumnew+=int(i)**numberdigit
#       return sumnew
   
#    if sumnew==number:
#       return True
#    else:
#       return False
# number=int(input("Enter your number : "))
# if armstrong(number):
#    print("number is armstrong")
# else:
#    print("not")


def arm(number):
   numberstr=str(number)
   numberdigit=len(numberstr)
   sumnew=0
   for i in numberstr:
      sumnew+=int(i)**numberdigit
   
   if sumnew==number:
      return True 
   else:
      return False
   

number=int(input("Enter your number : "))
if arm(number):
   print("arm")
else:
   print("not arm")
