print("Begin")

x="praneeth learning python"
y=x.split()
z=[[w.upper(),w.lower(),w.capitalize(),len(w )] for w in y]
for p in z:
    print(p)

print("End")
