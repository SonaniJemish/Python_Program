import time

ts = time.strftime('%H : %M : %S')
print("Time : ",ts)

tsh = int(time.strftime('%H'))
if(tsh>6 and tsh<=12):
    print("Good Morning")
elif(tsh>12 and tsh<=16):
    print("Good Afternoon")
elif(tsh>16 and tsh<=22):
    print("Good Evening")
else:
    print("Good Night")