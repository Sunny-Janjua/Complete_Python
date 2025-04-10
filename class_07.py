print("Function in python")

print("A function is a block of organized code written to carry out a specified task.")
print("Functions help break our program into smaller and modular chunks for better readability.")
print("Information can be passed into a function as arguments.")
print("Parameters are specified after the function name inside the parentheses.")
print("We can add as many parameters as we want. Parameters must be separated with a comma.")
print("A function may or may not return data.")
print("In Python a function is defined using the def keyword")

def hello():
    print("Hello World")
hello()

print("Parameter VS Argument in python")
print("A parameter is the variable listed inside the parentheses in the function definition.")
print("An argument is the value that is sent to the function when it is called.")
print("A parameter is the variable listed inside the parentheses in the function definition.")
print("An argument is the value that is sent to the function when it is called.")


def details(name,userid,country): # Function to print User details
 print('Name :- ', name)
 print('User ID is :- ', userid)
 print('Country :- ',country)

details('Asif' , 'asif123' , 'India')


def even_odd (num): #Even odd test
 """ This function will check whether a number is even or odd"""
 if num % 2 ==0:
     print (num, ' is even number')
 else:
     print (num, ' is odd number')
even_odd(3)
even_odd(4)
print(even_odd.__doc__)


# def myfunc1():
#  var2 = 10 # Variable with Local scope
#  print(var2)
# def myfunc2():
#  print(var2) # This will throw error because var2 has a local scope. Var2 is o
# myfunc1()
# myfunc2()

def myfunc1():
    var2 = 10 # Variable with Local scope
    print(var2)
var2 = 20 # Variable with Global scope
def myfunc2():
    print(var2)
myfunc1()
myfunc2()
print(var2)


list1 = [11,22,33,44,55]
print(list1)
def myfunc():
    del list1[2]
myfunc()
print(list1)

a = 10
b = 20

# Swapping values without a third variable using arithmetic operations
a = a + b
b = a - b
a = a - b

print(a)  # Output: 20
print(b)  # Output: 10

# Swapping values without a third variable using arithmetic operations
a = 10
b = 20
a = a * b
b = a / b
a = a / b

print(a)  # Output: 20
print(b)  # Output: 10

print("Factirial of a number")
def factorial(n):
   for i in range(1,n):
         n = n * i
   return n
print(factorial(5))

print("Factorial using recursion")
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))


def add(num): # Sum of first n natural numbers
 if num == 0:
    return 0
 else:
    return num + add(num-1)
print(add(5))

def add(num): # Sum of first n natural numbers
   sum = 0
   for i in range(1,num+1):
       sum = sum + i
   return sum
print(add(5))


# def fiboacci(num):
#  if num <= 1:
#     return num
#  if num == 2:
#     return 1
#  else:
#     return(fiboacci(num-1) + fiboacci(num-2))
# nums = int(input("How many fibonacci numbers you want to generate -"))
# for i in range(nums):
#  print(fiboacci(i)) 


# def fiboacci(num):
#    if num <= 1:
#       return num
#    if num==2:
#     return 1
#    else:
#       return(fiboacci(num-1) + fiboacci(num-2))
# nums = int(input("How many fibonacci numbers you want to generate -"))
# for i in range(nums):
#     print(fiboacci(i))


# def fiboacci(num):
#    if num<=1:
#       return num
#    if num==2:
#         return 1
#    else:
#       return(fiboacci(num-1) + fiboacci(num-2))
# nums = int(input("How many fibonacci numbers you want to generate -"))
# for i in range(nums):
#     print(fiboacci(i))


print("args & kwargs in python")
print("args and kwargs are mostly used in function definitions.")
print("args and kwargs allow you to pass a variable number of arguments to a function.")
print("args are used to send a non-keyworded variable length argument list to the function.")
print("kwargs are used to send a keyworded variable length argument list to the function.")
print("args and kwargs are mostly used in function definitions.")
print("args and kwargs allow you to pass a variable number of arguments to a function.")
print("args are used to send a non-keyworded variable length argument list to the function.")
print("kwargs are used to send a keyworded variable length argument list to the function.")
print("args and kwargs are mostly used in function definitions.")
print("args and kwargs allow you to pass a variable number of arguments to a function.")
print("args are used to send a non-keyworded variable length argument list to the function.")

print("args")
print("When we are not sure about the number of arguments being passed to a function then we can")
print("use *args as function parameter.")
print("*args allow us to pass the variable number of Non Keyword Arguments to function.")
print("We can simply use an asterisk * before the parameter name to pass variable length")
print("arguments.")
print("The arguments are always passed as a tuple.")
print("We can rename it to anything as long as it is preceded by a single asterisk (*). It's best")
print("practice to keep naming it args to make it immediately recognizable")

def args(*args):
    for i in args:
        print(i)
args(1,2,3,4,5)


print("**kwargs")
print("When we are not sure about the number of Keyword Arguments being passed to a function then we can")
print("**kwargs allows us to pass the variable number of Keyword Arguments to the function.")
print("We can simply use an double asterisk ** before the parameter name to pass variable length")
print("arguments.")
print("The arguments are passed as a dictionary.")
print("We can rename it to anything as long as it is preceded by a double asterisk (**). It's best")
print("practice to keep naming it kwargs to make it immediately recognizable.")


def kwargs(**kwargs):
    for key, value in kwargs.items():
        print(key, value)
kwargs(name='Asif', age=25, country='India')


def add1(*args):
   return sum(args)

print(add1(1,2,3))
print(add1(1,2,3,4))
print(add1(1,2,3,4,5))
print(add1(1,2,3,4,5,6))
print(add1(1,2,3,4,5,6,7))

list1 = [1,2,3,4,5,6,7]
list2 = [1,2,3,4,5,6,7]
list3 = [1,2,3,4,5,6,7]
list4 = [1,2,3,4,5,6,7]
print("Sum of all the elements in the list")
print(add1(*list1 , *list2 , *list3 , *list4 ))


def UserDetails(licenseNo, *args , phoneNo=0 , **kwargs): # Using all four argum
 print('License No :- ', licenseNo)
 j=''
 for i in args:
     j = j+i
 print('Full Name :-',j)
 print('Phone Number:- ',phoneNo)
 for key, val in kwargs.items():
     print("{} :- {}".format(key, val))


name = ['Asif' , ' ' , 'Ali' , ' ','Bhat']
mydict = {'Name': 'Asif', 'ID': 7412, 'Pincode': 41102, 'Age': 33, 'Country': 'India'}
UserDetails('BHT145' , *name , phoneNo=1234567890,**mydict )
