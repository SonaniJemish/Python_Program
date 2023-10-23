# doc sting always write below first line of function

def square(n):
    '''take one number ,return square of n'''
    print("Square of ",n," : ",n**2)

square(6)

print(square.__doc__) #to print comment which is store in function