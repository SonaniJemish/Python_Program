# same like switch case

x = int(input("Enter value of x : "))

match x: 
    case 0:
        print("x is 0")
    case 2:
        print("x is 2")
    case _ if x==4:
        print("x is 4")
    case _ if x!=4 and x==5:
        print("x is not 4, it is 5")
    case _:  #use to default case
        print(x)