from itertools import permutations
lst=input()
i=lst[-1]
lst=list(lst)
lst.remove(i)
lst.remove(lst[-1])
lst=sorted(lst)
lst=''.join(lst)
a=list(permutations(lst,int(i)))
for j in a:
    print(''.join(j))
