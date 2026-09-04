n=list(map(int,input("Enter elements into array:").split(',')))
a=len(n)
for i in range(a-1,0,-1):
    print(n[i],n[i-1],n[i]==n[i-1])
    
