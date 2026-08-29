x=0
y=1
a=int(input("Enter for how many times:"))
for i in range(a):
    print(x,end="")
    if i < a-1:
        print(",",end="")
    x,y=y,x+y
