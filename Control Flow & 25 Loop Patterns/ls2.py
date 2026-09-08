a=list(map(int,input("Enter numbers into the list:").split(',')))
b=int(input("Enter number to search:"))
def lsearch(a,b,i):
    if len(a)==i:
        return -1
    if b not in a:
        return -1
    if a[i]==b:
        return i
    return lsearch(a,b,i+1)
print(lsearch(a,b,0))


    

