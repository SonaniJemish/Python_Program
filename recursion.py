def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))
# how work
#  5 * factorial(4)
#  5 * 4 factorial(3)
#  5 * 4 * 3 factorial(2)
#  5 * 4 * 3 * 2 factorial(1)
#  5 * 4 * 3 * 2 * 1



# fibonacci squence

def fibo(n):
    if (n==0):
        return 0 
    elif (n==1 or n==2):
        return 1
    else:
        return fibo(n-1) + fibo(n-2) 

for n in range(10):
    print(fibo(n))
