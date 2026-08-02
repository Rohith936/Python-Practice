num = 48391
a=int(num//10e3)
b=num//10e2
c=int(b%10)
d=num//10e1
e=int(d%10)
f=num//10
g=int(f%10)
h=int(num%10)
print(f"Reverse:{h}{g}{e}{c}{a}")

