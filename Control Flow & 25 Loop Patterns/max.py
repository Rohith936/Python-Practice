x=int(input("x:"))
y=int(input("y:"))
z=int(input("z:"))
if x>y and x>z:
    print("x is largest")
elif y>x and y>z:
    print("y is largest")
elif z>y and z>x:
    print("z is largest")
else:
    print("Enter different values")
    
