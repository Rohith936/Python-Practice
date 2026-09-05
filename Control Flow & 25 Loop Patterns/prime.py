n=int(input("Upto how many numbers:"))
a=n
for i in range(1,n):
    if i*a==a:
        print(i)
    a-=1
        
