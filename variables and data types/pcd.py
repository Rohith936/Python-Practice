code = 23071549
a=code//10e5
print(f"Manufacturing year :20{int(a)}")
e=code%10e5
f=e//10e3
print(f"Month :{int(f)}")
c=code%10e3
d=c//100
print(f"Day :{int(d)}")
b=code%100
print(f"Product id :{b}")
