#break statement
print("Break Statement Program Start : \n")
for i in range(15):
    if(i==10):
        print("Skip after all argument 11 to 15 because break at i==10")
        break
    print("8 x ",i+1," = ",8*(i+1))


print("\n\n\n")

#continue statement

print("Continue Statement Program Start : \n")
for i in range(15):
    if(i==10):
        print("Skip i = 11 condition but next continue like 12,13,14, and 15")
        continue
    print("8 x ",i+1," = ",8*(i+1))