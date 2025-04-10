print("Now Defined Sets in python and defined its methods in detial")

print("1) Unordered & Unindexed collection of items.")
print("2) Set elements are unique. Duplicate elements are not allowed.")
print("3) Set elements are immutable (cannot be changed).")
print("4) Set itself is mutable. We can add or remove items from it.")

print("Set in python")
s = {10,20,30,40,50}
print(s)

myset={1}
print(myset)
print(type(myset))

my_set = {1,1,2,2,3,4,5,5}
print(my_set)


myset1 = {1.79,2.08,3.99,4.56,5.45}
print(myset1)

myset3 = {10,20, "Hola", (11, 22, 32)} # Mixed datatypes
print(myset3)


my_set1 = set(('one' , 'two' , 'three' , 'four'))
print(my_set1)


myset = {'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight'}
print(myset)
for i in myset:
  print(i)

print("Add elements to a set")
for i in enumerate(myset):
 print(i)

print("Add membership elements to a set")
print('one' in myset)
print('nine' in myset)


if 'three' in myset: # Check if 'three' exist in the set
 print('Three is present in the set')
else:
 print('Three is not present in the set')

print("Add elements to a set")
myset.add('nine')
print(myset)
myset.pop()
print(myset)

myset.update([1,2,3,5,6,7,8,9,7,6,4,3,3])
print(myset)

# myset.remove("nine")
# print(myset)


# myset.discard("five")
# print(myset)

# myset.clear()
# print(myset)


myset = {'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight'}
myset2=myset.copy()
myset1=myset

print(id(myset))
print(id(myset1))
print(id(myset2))


myset = {'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight'}
myset.add("hello world")
print(myset)

A = {1,2,3,4,5}
B = {4,5,6,7,8}
C = {8,9,10}

print(A.union(B).union(C))


"""
Updates the set calling the update() method with union of A , B & C.
For below example Set A will be updated with union of A,B & C.
"""
A.update(B,C)
print(A)


A = {1,2,3,4,5}
B = {4,5,6,7,8}

print(A.intersection(B))


"""
Updates the set calling the intersection_update() method with the intersection of
For below example Set A will be updated with the intersection of A & B.
"""
A.intersection_update(B)
print(A)

print(A.difference(B))



"""
Updates the set calling the difference_update() method with the difference of set
For below example Set B will be updated with the difference of B & A.
"""
B.difference_update(A)
print(B)

A = {1,2,3,4,5}
B = {4,5,6,7,8}
print(A.symmetric_difference(B))


"""
Updates the set calling the symmetric_difference_update() method with the symmetr
For below example Set A will be updated with the symmetric difference of A & B.
"""
A.symmetric_difference(B)
print(A)


A = {1,2,3,4,5,6,7,8,9}
B = {3,4,5,6,7,8}
C = {10,20,30,40}

print(B.issubset(A))
print(A.issuperset(B))
print(C.isdisjoint(A))
print(B.isdisjoint(A) )