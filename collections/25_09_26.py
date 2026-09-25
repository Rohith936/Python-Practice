#1
'''
from collections import Counter
nums = (1, 1, 1, 2, 2, 3, 4, 4, 4, 5)
k = 2
nums=Counter(nums)
print(nums.most_common(k))
'''
#1-2
'''
nums = (1, 1, 1, 2, 2, 3, 4, 4, 4, 5)
k = 2
dic={}
for i in nums:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
a=[]
for i in range(k):
    a.append(max(dic.values()))
c=len(a)-1
while c>=0:
    b=[key for key,value in dic.items() if value==a[c]]
    c-=1
print(b)

nums = (1, 1, 1, 2, 2, 3, 4, 4, 4, 5)
k = 2
dic = {}
# Count frequency
for i in nums:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
# Find top k elements
result = []
for _ in range(k):
    max_value = max(dic.values())

    for key, value in dic.items():
        if value == max_value:
            result.append(key)
            del dic[key]
            break
print(result)
'''
#2
a = (
    (1, 3),
    (2, 6),
    (8, 10),
    (15, 18)
)
