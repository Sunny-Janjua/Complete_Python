print("hello World")
from gc import collect
import sys
import keyword
import operator
from datetime import datetime
import os

from traitlets import This


print(keyword.kwlist)
print(len(keyword.kwlist))
print(keyword.iskeyword("if"))
print(keyword.issoftkeyword("async"))

print("key world list")


print("single line statement")
p1 = 10 + 20
print(p1)

print("Single line statement")
p2 = ['a' , 'b' , 'c' , 'd']
print(p2)

print(' Multiple line statement')
p1 = 20 + 30 \
 + 40 + 50 +\
 + 70 + 80

print(p1)

print(' Multiple line statement')
sunny=4443+3444\
+343444

print(sunny)


print("Multiple line statement")

p2 = ['a' ,
 'b' ,
 'c' ,
 'd'
 ]
print(p2)


print("Correct way to define iderntifier")

p = 10
if p == 10:
 print ('P is equal to 10') 

print("Correct way to create identition in python to take tab/space in python ok!")

for i in range(0,5):
 print(i) 



print("Correct way to create identition in python to take tab/space in python ok!")

for i in range(5): print(f" our i : {i}")

for i in range(0,5): print(i) # correct indentation but less readable


print("Nested loop in python!")

j=20
for i in range(0,5):
 print(i) # inside the for loop
print(j) # outside the for loop

print("Print * using loop in python")

for i in range(0,10):
 print(i*"*")



print("Print * using loop in python")
number:int=10

while(number>0):
 print(number*"*")
 number-=1


def doc():
 """
 hello well come to code wtih sunny janjua 
 learn html css js ts and react and next and backend!
 """
 print("Hello doc string in python")

print(doc.__doc__)
doc() 

def square(num):
 '''Square Function :- This function will return the square of a number'''
 return num**2
print(square.__doc__)
sqr=square(44444)
print(sqr)


def evenodd(num):
 '''evenodd Function :- This function will test whether a numbr is Even or Odd'
 '''
 if num % 2 == 0:
    print("Even Number")
 else:
    print("Odd Number")
print(evenodd.__doc__)
evenodd(5554)

'''
id() function returns the “identity” of the object.
The identity of an object - Is an integer
 - Guaranteed to be unique
 - Constant for this object during its lifetime.
'''


sunny="code with sunny janjua"
print(sunny)
print(id(sunny))
print(hex(id(sunny)) )


number1=10
number2=10
number3=number1

print(number1)
print(id(number1))
print(number2)
print(id(number2))
print(number3)
print(id(number3))

print("Variables is defined as line by line !")

intvar = 10 # Integer variable
floatvar = 2.57 # Float Variable
strvar = "Python Language" # String variable
print(intvar)
print(floatvar)
print(strvar)

print("Variables is defined in one line !")

intvar , floatvar , strvar = 10,2.57,"Python Language" # Using commas to separate
print(intvar)
print(floatvar)
print(strvar)

print("All variables pointing to same value")

p1 = p2 = p3 = p4 = 44 # All variables pointing to same value
print(p1,p2,p3,p4)


print("Now find size and datatypes of variables in python!")

num1=444
print(num1)
print(type(num1))
print(sys.getsizeof(num1))
print(isinstance(num1,float))

number=443344
print(number)
print(sys.getsizeof(int()) )

print(True==1)
print(True==0)
print(False==0)
print(False==1)

print("String Method and string defination!")

str="hello world"

print(str)

str1 = "HELLO PYTHON"
print(str1)

mystr = 'Hello World' # Define string using single quotes
print(mystr)


mystr = '''Hello
 World ''' # Define string using triple quotes
print(mystr)


mystr = ('Happy '
 'Monday '
 'Everyone')
print(mystr)

mystr2 = 'Woohoo '
mystr2 = mystr2*5

print(mystr2)


string="hello world"
print(string)
for i in string:
 print(i*5)
 print(len(i*5))

print("After loop!")


string = "code with sunny janjua !"
print(string)
print(string[3])
print(string[2:6])
print(string[-1])

new_string="hello world"
# del new_string
# del string is working mean del value's !
print(new_string)


print("STRING METHOD SI START!")
# String concatenation
s1 = "Hello"
s2 = "Asif"
s3 = s1 + s2
print(s3)

# String concatenation
s1 = "Hello"
s2 = "Asif"
s3 = s1 + " " + s2
print(s3)


string = "code with sunny!"
for i in enumerate(string):
 print(i)

print("Check is IN stirng value")
stirng = "code with sunny janjua !"
print("wiht" in string)
print("with" in string)

"""
The partition() method searches for a specified string and splits the string into
 - The first element contains the part before the argument string.
 - The second element contains the argument string.
 - The third element contains the part after the argument string.
"""
str5 = "Natural language processing with Python and R and Java"
L = str5.partition("and") 
print(L)

"""
The rpartition() method searches for the last occurence of the specified string a
containing three elements.
 - The first element contains the part before the argument string.
 - The second element contains the argument string.
 - The third element contains the part after the argument string.
"""
str5 = "Natural language processing with Python and R and Java"
L = str5.rpartition("and")
print(L)


print("STRING METHOD IS DEFINED NOW!")

mystr2 = " Hello Everyone "
print(mystr2)
print(mystr2.strip())
print(mystr2.lstrip())
print(mystr2.rstrip())


mystr2 = "*********Hello Everyone***********All the Best**********"
print(mystr2)
print(mystr2.strip("*"))
print(mystr2.lstrip("*"))
print(mystr2.rstrip("*"))


string="code with sunny !"
print(string.upper())
print(string.lower())
print(string.upper())
print(string.replace("sunny","hussnianmulazam"))

print(string.count("code"))
print(string.startswith("code"))
print(string.endswith("code"))
print(string)
print(string.startswith("!"))
print(string.endswith("!"))

mystr4 = "one two three four one two two three five five six seven six seven one"
print(mystr4.split())


mylist = mystr4.split() 
print(mylist)

print("FORMATED STRING IS PRINTED NOW ")

my_stirng= "one{} two{} three{} four{} five{} six{}"
str1=1
str2=2
str3=3
str4=4
str5=5
str6=6

print(my_stirng.format(str1,str2,str3,str4,str5,str6))


# Combining string & numbers using format method
item1 = 40
item2 = 55
item3 = 77
res = "Cost of item3 , item2 and item1 are {2} , {1} and {0}"
print(res.format(item1,item2,item3))

str2 = " WELCOME EVERYONE "
str2 = str2.center(100) # center align the string using a specific character as t
print(str2)


str2 = " WELCOME EVERYONE "
str2 = str2.center(50,'*') # center align the string using a specific character
print(str2)


str2 = " WELCOME EVERYONE I AM SUNNY JANJUA"
str2 = str2.rjust(50,*"*") # Right align the string using a specific character as the
print(str2)
str2 = str2.ljust(50,*"*") # Right align the string using a specific character as the
print(str2)


str4 = "one two three four five six seven"
loc = str4.index("five") # Find the location of word 'five' in the string "str4"
print(loc)


str4 = "one two three four five six seven"
loc = str4.find("five") # Find the location of word 'five' in the string "str4"
print(loc)


mystr6 = '123456789'
print(mystr6.isalpha()) # returns True if all the characters in the text are lett
print(mystr6.isalnum()) # returns True if a string contains only letters or numb
print(mystr6.isdecimal()) # returns True if all the characters are decimals (0-9)
print(mystr6.isnumeric()) 


mystr6 = 'abcde'
print(mystr6.isalpha()) # returns True if all the characters in the text are lett
print(mystr6.isalnum()) # returns True if a string contains only letters or numb
print(mystr6.isdecimal()) # returns True if all the characters are decimals (0-9)
print(mystr6.isnumeric()) 


mystr6 = 'abc12309'
print(mystr6.isalpha()) # returns True if all the characters in the text are lett
print(mystr6.isalnum()) # returns True if a string contains only letters or numb
print(mystr6.isdecimal()) # returns True if all the characters are decimals (0-9)
print(mystr6.isnumeric()) 

mystr6 = 'abc12309'
print(mystr6.isalpha()) # returns True if all the characters in the text are lett
print(mystr6.isalnum()) # returns True if a string contains only letters or numb
print(mystr6.isdecimal()) # returns True if all the characters are decimals (0-9)
print(mystr6.isnumeric())

mystr6 = 'abc12309'
print(mystr6.isalpha()) # returns True if all the characters in the text are lett
print(mystr6.isalnum()) # returns True if a string contains only letters or numb
print(mystr6.isdecimal()) # returns True if all the characters are decimals (0-9)
print(mystr6.isnumeric()) 


# mystr = "My favourite TV Series is "\Game of Thrones""   this is wrong statement decleration in python

#Using escape character to allow illegal characters
mystr = "My favourite series is \"Game of Thrones\""   #This is collect way to define string 
print(mystr)
