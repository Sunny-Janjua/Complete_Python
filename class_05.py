print("Dictionary in python")


print("Dictionary is a mutable data type in Python.")
print("A python dictionary is a collection of key and value pairs separated by a colon (:) & enclosed")
print("in curly braces {}.")
print("Keys must be unique in a dictionary, duplicate values are allowed.")
print("Keys are immutable, values are mutable.")

mydict = {}
print(mydict)
print(type(mydict))

mydict={
    "name":"hussnain mulazam",
    "roll_no":4555,
    "is_student":True
}
print(mydict)
print(mydict.keys())
print(mydict.values())

print(mydict.items())

mydict1 = {1:'one' , 2:'two' , 'A':['asif' , 'john' , 'Maria'], 'B':('Bat' , 'cat')}
mydict2 = {1:'one' , 2:'two' , 'A':['asif' , 'john' , 'Maria']} # dictionary with 
print(mydict1)
print(mydict2)


keys = {'a' , 'b' , 'c' , 'd'}
mydict3 = dict.fromkeys(keys) # Create a dictionary from a sequence of keys
print(mydict3)


mydict4 = dict.fromkeys(keys, 10) # Create a dictionary from a sequence of keys with value 10
print(mydict4)

mydict5 = dict.fromkeys(keys, 'value') # Create a dictionary from a sequence of keys with value 'value'
print(mydict5)

keys = {'a' , 'b' , 'c' , 'd'}
value = 10
mydict3 = dict.fromkeys(keys , value) # Create a dictionary from a sequence of k
print(mydict3)


keys = {'a' , 'b' , 'c' , 'd'}
value = [10,20,30]
mydict3 = dict.fromkeys(keys , value) # Create a dictionary from a sequence of k
print(mydict3)

value.append("hello world")
print(mydict3)

mydict = {1:'one' , 2:'two' , 3:'three' , 4:'four'}
print(mydict)
print(mydict.get(3))
print(mydict.get(4))

print(mydict.get(5))
print(mydict.get(5 , "Key Not Found!"))

mydict = {1:'one' , 2:'two' , 3:'three' , 4:'four'}
print(mydict)
print(mydict.pop(3))
print(mydict)

mydict = {1:'one' , 2:'two' , 3:'three' , 4:'four'}
print(mydict)
print(mydict.popitem())
print(mydict)

mydict = {1:'one' , 2:'two' , 3:'three' , 4:'four'}
print(mydict)
mydict.clear()
print(mydict)

mydict = {1:'one' , 2:'two' , 3:'three' , 4:'four'}
print(mydict)
mydict1 = mydict.copy()
print(mydict1)
print(id(mydict))
print(id(mydict1))

mydict1[5]="hello world"
print(mydict)
print(mydict1)

mydict = {1:'one' , 2:'two' , 3:'three' , 4:'four'}
mydict1 = mydict
print(mydict)
print(mydict1)
print(id(mydict))
print(id(mydict1))


mydict = {1:'one' , 2:'two' , 3:'three' , 4:'four'}
for key,value in mydict.items():
    print(key,value)


print("SORTED DICTIONARY IN PYTHON USIGN SORTNG METHOD!")
print("Sorting dictionary by key")
print("Dictionary Comprehension is a concise way to create dictionary. It is similar to list comprehension.")
print("Dictionary comprehension consists of an expression pair (key: value) followed by for statement inside curly braces {}.")


mydict = {1:'one' , 3:'three' , 2:'two' , 4:'four'}
print(mydict)

mydict={i:i*5 for i in range(1,6)}
for i in mydict:
    print(i,mydict[i])
print(mydict)


key = ['one' , 'two' , 'three' , 'four' , 'five']
value = [1,2,3,4,5]
mydict = {k:v for (k,v) in zip(key,value)} # using dict comprehension to create d
print(mydict)


string="hello world"
print(string)
mydict={k:v*5 for k,v in enumerate(string)}
print(mydict)

str1 = "Natural Language Processing"
mydict2 = {k:v for (k,v) in enumerate(str1)} # using dict comprehension to create dictionary
print(mydict2)


str1 = "abcdefghijklmnopqrstuvwxyz"
mydict3 = {i:i.upper() for i in str1}
print(mydict3)



mystr4 = "one two three four one two two three five five six seven six seven one one"
mydict={k:v for k,v in enumerate(mystr4)}
print(mydict)