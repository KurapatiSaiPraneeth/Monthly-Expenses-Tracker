print("Begin")
mylist=[]
for i in range(5):
    if i==1:
        mylist.append(input("Enter first number:"))
    elif i==2:
        mylist.append(input("Enter second number:"))
    elif i==3:
        mylist.append(input("Enter third number:"))
print(mylist)
sum=0
for p in mylist:
    i=int(p)
    sum=sum+i
print(sum)        
print("End")
