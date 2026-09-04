n=list(map(int,input("Enter elements into array:").split(',')))
k=int(input("Chunk upto:"))
a=k
g=k
m=0
for i in range(0,len(n),k):
    while g>=0:
        print(n[m:k])
        m+=a
        k+=k
        g-=1
        
    
   
