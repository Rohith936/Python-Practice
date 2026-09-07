n=input("Enter a string to check palindrome:\n")
def pal(n):
    while i:
        i=len(n)
        i-=1
        n+=''+n[i-1]
    return n
print(pal(n))
