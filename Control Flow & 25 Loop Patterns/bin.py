n=int(input())
n=bin(n)
print(f"{str(n)[2:]}")
i=int(input())
a=''
while i>0:
    bit=i%2
    bit=str(bit)
    a=a+bit
    i//=2
print(a[::-1])
