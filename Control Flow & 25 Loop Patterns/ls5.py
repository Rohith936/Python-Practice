n=int(input())
i=input()
ls=['sun','mon','tue','wed','thur','fri','sat']
n=(n+ls.index(i))%7
print(ls[n])
