print("Begin")
x=[10,20,30,40,50]
print("Given list",x)
x.append(50)
print("50 is appended again:",x)
print(x.count(50),"times 50 is repeated in a List!")
print("50 is in a Index of",x.index(50))
x.insert(0,90)
print("90 is inserted at the index of 0")
print("50 is removed from a List:",x.remove(50))
print(x)
y=[90,80,70]
x.extend(y)
print(x)
z=x.copy()
print(z)
z.sort(reverse=True)
print(z)
z.reverse()
print(z)
z.clear()
print(z)

print("End")
