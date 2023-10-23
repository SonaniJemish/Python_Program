list1 = [11,12,5,2,3,55,68,96,78,52,100]
print(list1,end="\n\n")
list1.append(45)   #data ko last me add karne ke liye
print(list1,end="\n\n")
list1.reverse()   #list ko reverse me print karega bina sort kiye
print(list1,end="\n\n")
list1.sort()   # list ko sort karega
print(list1,end="\n\n")
list1.sort(reverse=True)   #list ko reverse me sort karega
print(list1,end="\n\n\n")


print(list1)
print(list1.index(55),end="\n\n\n")     # show index of value



print(list1)
print(list1.count(55),end="\n\n\n")    # show howmany time value in list

# to copy list , if we use newlist=oldlist that time it is use referance each other and if we change any value from any list value must change in both list so use copy methoz
newlist = list1.copy() 
newlist[0] = 65
print(list1)
print(newlist)


# insert value in perticular index
list1.insert(2,2222)
print(list1,end="\n\n\n")


# extend method use to mearge 2 list
color1 = ["Blue","Black"]
print("Color 1 : ",color1)
color2 = ["White","Red"]
print("Color 2 : ",color2)
color1.extend(color2)
print("Color mearge : ",color1)