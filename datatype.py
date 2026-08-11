a = 1   # this is int type
b = "Jemish"    # this is str type
c = True    # this is bool type
d = None    # this is none type
print(f"value of a : {a}")
print("Type of a : ",type(a), end="\n\n")
print(f"value of b : {b}")
print("Type of b : ",type(b),end="\n\n")
print(f"value of c : {c}")
print("Type of c : ",type(c),end="\n\n")
print(f"value of d : {d}")
print("Type of d : ",type(d),end="\n\n")
print("-"*100,"\n")




list1 =  [8,1.2,[-4,5],"apple"]  #here you can add different type of value
print("list : ",list1,end="\n\n")
# below we can see how to get value from list
print(f"list's first value : {list1[0]}  -- here first value index is 0")
print(f"list's third value : {list1[2]}  -- here third value index is 2")
print(f"list's inside list's first value : {list1[2][0]}  -- here value index is [2][0]\n")
print("-"*100,"\n")




tuple1 =  (8,78.2,[-4,5],"apple")  #here you can add different type of value, but you can not change value
print("tuple : ",tuple1)
print("Note : You can not change the value in tuple",end="\n\n")
# below we can see how to get value from tuple
print(f"tuple's first value : {tuple1[0]}  -- here first value index is 0")
print(f"tuple's third value : {tuple1[2]}  -- here third value index is 2")
print(f"tuple's inside list's first value : {tuple1[2][0]}  -- here value index is [2][0]\n")
print("-"*100,"\n")




dictionary = {"name":"Jemish","age":"21","gender":"male"}
print(f"Dictionary : {dictionary}\n")
# Below we can see how to get single value from Dictionary
print(f"Name : {dictionary['name']}")
print(f"Age : {dictionary['age']}")
print(f"Gender : {dictionary['gender']}\n")
print("-"*100,"\n")




# Convert datatype into different datatype
print("Below method is convert into different datatype using : int(),float(),str(),ord(),hex(),oct(),tuple(),set(),list(),dict()")
a="1"
print(f"a = {a}, and Type : {type(a)} ")
b="2.5"
print(f"b = {b}, and Type : {type(b)} ")
print(f"int(a)+flot(b) = total \n1+2.5 = {int(a)+float(b)}\n")  #also you can convert into different datatype using : int(),float(),str(),ord(),hex(),oct(),tuple(),set(),list(),dict()
print("-"*100,"\n")




set1 = {1,2,3,4,1}
set2 = {4,6,7,8}
print(f"Set 1 : {set1} \nSet 2 : {set2}")
print("Note : Sets does not allowed duplicate value\n")
# set1.clear()
# print(f"Set Clear: {set1}")
set1.add(1000)
print(f"Set after add 1000 : {set1}")
set1.remove(1000)
set1.discard(1000)  # discard not throw the error if value is not in set
print(f"Set after remove 1000 : {set1}")
print(f"Union of sets : {set1.union(set2)}  -- you can use 'set1 | set2' also")
print(f"Intersection of sets : {set1.intersection(set2)}  -- you can use 'set1 & set2' also")
print(f"Difference of sets : {set1.difference(set2)}  -- you can use 'set1 - set2' also")
print(f"Symmetric Difference of sets : {set1.symmetric_difference(set2)}  -- you can use 'set1 ^ set2' also")
print(f"Value 2 in set1 check : {2 in set1}\n")
print("-"*100,"\n")
