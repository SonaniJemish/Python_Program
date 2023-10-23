para = "Hello, My name is {} and I am from {}"
name="Jemish"
country="Bharat"

print(para.format(name,country))
print(para.format(country,name),end="\n\n\n") # print alternet


# so we use index method

para1 = "Hello, My name is {1} and I am from {0}"
name="Jemish"
country="Bharat"


print(para1.format(country,name),end="\n\n\n")


# usinf f string
print(f"Hello, maru name {name} chhe ane hu {country} ma rahu chhu.",end="\n\n\n")
print(f"Hello, maru name {{name}} chhe ane hu {{country}} ma rahu chhu.",end="\n\n\n")  #show as it is as i write

number=5.696
txt=f"this is flot number : {number:.2f}"
print(txt)