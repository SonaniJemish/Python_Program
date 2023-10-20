num = int(input("Enter Number : "))

if(num<0):
    print("Number is Negative")
elif(num>0):
    if(num<=10):
        print("Number between 0 to 10")
    elif(num>10 and num<=20):
        print("Number between 11 to 20")
    else:
        print("Number is graterthan 20")
else:
    print("Number is Zero")
