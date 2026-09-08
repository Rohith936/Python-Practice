a=int(input('a:'))
b=int(input('b:'))
def power(a,b):
    if b==0:
        return a
    return int((a**(b/2))**2)
print(power(a,b))

