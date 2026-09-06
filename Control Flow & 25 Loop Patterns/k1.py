n=int(input("Enter number for countdown:"))
k=int(input("skip multiple num:"))
for i in range(1,n+1):
    if i%k==0:
        continue;
    print(i)
