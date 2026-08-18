a=int(input("Enter length of side A:\n"))
b=int(input("Enter length of side B:\n"))
c=int(input("Enter length of side C:\n"))
if(a==b and b==c):
    print("Equilateral Triangle")
elif(a==b or a==c or b==c):
    print("Iso Triangle")
elif(a!=b and b!=c):
    print("Scalene Triangle")
    
