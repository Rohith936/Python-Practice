n=int(input('n:'))
r=int(input('r:'))
def C(n,r):
    if r==0 or r==n:
        return 1
    return C(n-1,r-1)+C(n-1,r)
print(C(n,r))


