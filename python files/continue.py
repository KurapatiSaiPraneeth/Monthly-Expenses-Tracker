print("Begin")
x=input("Enter any number:")
i=int(x)
print("welcome",i)
z=1
while z<=10:
    i+=1
    z+=1
    if z==3:
        print("third element is skipped by continue")
        continue
    print("welcome",i)
print("End")
