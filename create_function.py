# syntex

# def function_name (parameter):
#     pass    ----use when condition not define
#     code or statement


def sum_of_two_num (a,b):
    eq = a+b
    print(f"a + b = {eq}")



a=2
b=3
sumation = sum_of_two_num(a,b)


# Note : Sum is None because function doesn't return anything so we can not store any value in variable
print(f"\n\n a = {a} and b = {b} : Sum = {sumation}\n Note : Sum is None because function doesn't return anything \n\n")  #It returns None because the function doesn't return anything.

sum_of_two_num(9,1)





# (*number) shows argument take only numbera
# simple way me (a,b) aisa likh sakte hai  like "def average (a,b):"

def average (*number):
    sum=0
    for i in number:
        sum=sum+i
    return sum/len(number)

avg_ans = average(1,2,3,4,5,6)
print("Average : ",avg_ans)