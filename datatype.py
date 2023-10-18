a = 1   # this is int type
b = "Jemish"    # this is str type
c = True    # this is bool type
d = None    # this is none type
print(a)
print(b)
print(c)
print(d,end="\n\n")
print("Type of a : ",type(a))
print("Type of b : ",type(b))
print("Type of c : ",type(c))
print("Type of d : ",type(d),end="\n\n")


list =  [8,8.2,[-4,5],"apple"]  #here you cad add different type of value and same function in tuple but you can not change value
print("list value : ",list,end="\n\n")

dictionary = {"name":"Jemish","age":"21","gender":"male"}
print(dictionary,end="\n\n")


# Convert datatype into different datatype
a="1"
b="2.5"
print(int(a)+float(b))  #also you can convert into different datatype using : int(),float(),str(),ord(),hex(),oct(),tuple(),set(),list(),dict()