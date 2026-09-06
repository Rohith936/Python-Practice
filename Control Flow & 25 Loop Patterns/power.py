a=int(input("Enter base:"))
b=int(input("Enter power:"))
def power(a,b):
    if b==0:
        return 1
    return a*power(a,b-1)
print(power(a,b))

