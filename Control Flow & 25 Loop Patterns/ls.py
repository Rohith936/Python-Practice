a=list(map(int,input("Enter numbers into the list:").split(',')))
b=int(input("Enter number to search:"))
def lsearch(a,b,i):
    if b not in a:
        return None
    if b in a:
        return a.index(b)
print(lsearch(a,b,0))


