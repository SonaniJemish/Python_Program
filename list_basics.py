list1 = [1,2,3.5,"Jemish",True]
print(list1)
print(list1[0])
print(list1[1])
print(list1[2])
print(list1[3])
print(list1[4],end="\n\n")


print(list1[-4])   # negative index
print(list1[len(list1)-4])   #convert in to positive index  == lenth of list value minus negative value
print(list1[5-4])   # convert in to positive index  
print(list1[1],end="\n\n")   # positive index



if "Jemish" in list1:
    print("Yes")
else:
    print("No")


if "Jemi" in "Jemish":
    print("Yes")
else:
    print("No")
print("\n\n")


#print list value in diffrent way
print(list1[:])
print(list1)
print(list1[0:5])
print(list1[-5:5])
print(list1[0:5:2])
print(list1[::2])
print(list1[0:5:3],end="\n\n")


#list comprehension

list2 = [i+1 for i in range(10)]
print(list2)