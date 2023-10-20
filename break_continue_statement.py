#break statement

for i in range(15):
    if(i==10):
        break
    print("8 x ",i+1," = ",8*(i+1))



#continue statement

for i in range(15):
    if(i==10):
        print("Skip i = 10 condition but next continue")
        continue
    print("8 x ",i+1," = ",8*(i+1))