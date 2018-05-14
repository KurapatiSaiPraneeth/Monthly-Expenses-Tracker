print("Begin")
x=input("Enter any number:")
i=int(x)
if i<10:
    print("Given number",i,"is a single digit number!")
elif i<100:
    print("Given number",i,"is a two digits number!")
elif i<1000:
    print("Given number",i,"is a three digits number!")
else:
    print("Given number",i,"is a greater than 3 digits number!")

print("Thank you for participation!")        
print("End")
