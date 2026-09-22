'''
from collections import Counter
c=Counter('consistency')
print(c['s'])
print(c.most_common(2))  #2 is value
print(c.most_common()[-1])   #least common
print(c)
print(c.most_common())
print(Counter(['a','b','a'])+Counter(['a']))

a = {"x": 1, "y": 2}
b = {"y": 9, "z": 3}
merged = {*a, *b} 
merged1={**a, **b}
print(merged)
print(merged1)
merged=a|b
a|=b
print(merged)
print(a)
#nested dict
records={'Asha':{'math':92,'cs':88},'Ravi':{'math':75,'cs':95}}
print(records['Asha']['cs'])


arr=[2,2,2,2]
print(list(set(arr)))
'''
