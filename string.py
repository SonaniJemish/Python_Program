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
print("print first 8 character  : ",names[0:len(names)-5],end="\n\n\n\n")


# stirngs are immutable
string = "hi !! Sonani Jemish !!!" 
print(string.upper(),end="\n\n") #convert into upper case
print(string.lower(),end="\n\n") #convert into lower case
print(string.rstrip("!"),end="\n\n") #rstip me jo element diya jaya hai wo remove karata hai but last vala only ( ex= hi !! Sonani Jemish)
print(string.replace("Jemish", "Sneha"),end="\n\n") #string me word change karata hai
print(string.split(" "),end="\n\n") #jaha space hoga vaha se new element  bana lega
print(string.capitalize(),end="\n\n\n\n") #first character ko capital and baki sabko smal me convert kar deta hai



#string ko center me lane ke liye use hota hai
str1 = "jemish"
print(str1)
print("str1 lenth : ",len(str1))
print(str1.center(10))
print("str1 lenth after center function use : ",len(str1.center(10)),end="\n\n\n\n")



# string me koi word or character kitni baar aata hai wo cheack karane ke liye count() function ka use hota hai
str2 = "Radhe Radhe"
print("how many time a in string  : ",str2.count("a"))
print("how many time radha in string  : ",str2.count("Radhe"),end="\n\n")

print(str2.endswith("e"))
print(str2.endswith("h",2,10))  #index 2 to 10 me string e se khatam hota hai
print(str2.endswith("h",2,11),end="\n\n")  #index 2 to 11 me string e se khatam hota hai

#find function     2. index function same use
str3 = "Hello i am jemish"
print(str3.find("am"),end="\n\n")  #kai index par chhe te batave chhe

# isalnum --- use to check alphabet and number are include in string
# isalpha --- use to check only alphabet include in string if number are available then show flase
# islower --- use to check all string characters are small
# isprintable --- use to check all character are printable or not
# isspace --- use to check any space are available in string