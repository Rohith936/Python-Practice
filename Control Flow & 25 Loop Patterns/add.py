n=int(input("Enter minimum of 2 digits:"))
def add(n):
    if n<=0:
        return 0
    return n%10+add(n//10)
print(add(n))
