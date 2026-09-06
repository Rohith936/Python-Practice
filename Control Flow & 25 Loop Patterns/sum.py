n=list(map(int,input("Enter the elements in to list:").split(',')))
def add(n):
    return sum(n)
print(add(n))
i=len(n)
def product(n):
    global i
    i-=1
    if i<0:
        return 1
    return n[i]*product(n)
print(product(n))
