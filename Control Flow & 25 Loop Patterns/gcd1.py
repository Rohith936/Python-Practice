import statistics
arr=list(map(int,input("Enter elements into array:").split(',')))
b=0
arr1=[]
for i in arr:
    n=1
    while n<=i:
        if i%n==0:
            arr1.append(n)
        n+=1
arr1.remove(1)
print(statistics.mode(arr1))
