i=10203040
print(int((str(i).replace('0',''))))
i=int(input())
a=int(str(i)[::-1])
b="True" if a>i else "False"
print(b)
