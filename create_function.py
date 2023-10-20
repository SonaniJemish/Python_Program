# syntex

# def function_name (parameter):
#     pass    ----use when condition not define
#     code or statement


def sum (a,b):
    eq = a+b
    print("Sum = ", eq)


a=2
b=3
sum(a,b)
sum(9,1)





#dictionary ke liye (**name)  use hota hai
# simple way me (a,b) aisa likh sakte hai

def average (*num):                  
    sum=0
    for i in num:
        sum=sum+i
    return sum/len(num)

ans = average(6,6,6,6,6,6)
print("Average : ",ans)