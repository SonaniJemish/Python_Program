# basic input mathod
a = input("Enter value of a :")
print(a)



# input me enter kareli value as a sting add thay chhe
a = input("Enter value of a : ")
b = input("Enter value of b : ")
print("a+b  = ",a+b)  #but yaha pe output me addition nahi hoga uski jagah par do sting mearge hogi (ex : a=2, b=2, output = 22)


# solution 1
# => input se pehale data type lakhi levani
a = int(input("Enter a : "))
b = int(input("Enter b : "))
print("a+b  = ",a+b)

# solution 2
# => print me veriable se pehale data type lakhi levani
a = input("Enter a : ")
b = input("Enter b : ")
print("a+b  = ",int(a)+int(b))