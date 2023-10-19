names = "Jemish,Sonani"

#len function se aap lenth jaan skte hai
# len = len(names)   
print("Lenth of names : ",len(names))

 #jo word print karana hai uski starting or ending index type karana hai 
 # agar aap string 0 se start karana chahate ho aur aap 0 nahi lagate to python apne aap 0 laga lega aisa same end ke liey bhi hota hai
print("print first word : ",names[0:6])
print("print first four character : ",names[0:4])


# negative type karate he to pytho negative ke aahe veriable ki full lenth laga leta hai
# ex : names ki lenth 13 hai aur usme -4 add karenge to 9 hoga to output me 0 se 9 [0:9] index ko consider karega
print("print first 9 character  : ",names[0:-4])
print("print first 8 character  : ",names[0:len(names)-5])