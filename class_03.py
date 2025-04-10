print("Tuple in python")

print("Tuple is similar to List except that the objects in tuple are immutable which means we cannot")
print("change the elements of a tuple once assigned.")
print("When we do not want to change the data over time, tuple is a preferred data type.")
print("Iterating over the elements of a tuple is faster compared to iterating over a list.")

tup=()
print(tup)
print(type(tup))

tup6 = (100, 'Asif', 17.765) 
tup5 = ('Asif', 25 ,(50, 100),(150, 90)) 
tup4 = ('one','two' , "three")
tup3 = (10.77,30.66,60.89) 
tup2 = (10,30,60) 

print(tup2)
print(tup3)
print(tup4)
print(tup5)
print(tup6)

mytuple = ('one' , 'two' , 'three' , 'four' , 'five' , 'six' , 'seven' , 'eight')
print(mytuple)
print(mytuple[3])
print(mytuple[2:5])

print(mytuple[-3:])

for i in mytuple:
 print(i)


for i in enumerate(mytuple):
 print(i)

mytuple1 =('one', 'two', 'three', 'four', 'one', 'one', 'two', 'three')
print(mytuple1.count("one"))


if 'three' in mytuple: # Check if 'three' exist in the list
 print('Three is present in the tuple')
else:
 print('Three is not present in the tuple')

print(mytuple.index('one')) 


print("SORTED TUPLE IN PYTHON USIGN SORTNG METHOD!")

mytuple2 = (43,67,99,12,6,90,67)
print(sorted(mytuple2))

mytuple2 = (43,67,99,12,6,90,67)
print(sorted(mytuple2 ,reverse=True))

