n=list(map(int,input("Enter elements into list:\n").split(',')))
a=len(n)-1
for j in range(a):
    for i in n:
        if n[0] > i:
            n[j]=i
            print(n)
