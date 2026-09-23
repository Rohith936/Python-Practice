'''
a=[1,2,3,4]
for i,val in enumerate(a):
    print(i,val)
for i,val in enumerate(a,start=1):
    print(i,val)
b=[6,5,4,2]
for i,j in zip(a,b):
    print(i,j)
'''
#defaultdict
'''
from collections import defaultdict
words = ["apple", "banana", "avocado", "cherry", "blueberry"]
by_letter = defaultdict(list)        #auto creates empty list
for w in words:
    by_letter[w[0]].append(w)      #key values are first letter of each word
print(by_letter)
    
counts=defaultdict(int)
for ch in 'consistency':
    counts[ch]+=1
print(counts)
'''
#frozenset
'''
fs=frozenset([1,2,3])
groups={frozenset({1,2}):'pair A',frozenset({3,4}):'pair B'}
print(groups)
'''
#two sum
'''
def two_sum(nums, target):
    for num in nums:
        need=target-num
        if need in nums:
            return [nums.index(num),nums.index(need)]
    return []
print(two_sum([7,11,15,2],9))
'''
#first 1
'''
from collections import Counter
def first_unique(s):
    counts=Counter(s)
    for ch in s:
        if counts[ch]==1:
            return ch
    return '_'
print(first_unique('consistency'))
'''
#most common
'''
from collections import Counter
def top_k(nums,k):
    return [val for val,_ in Counter(nums).most_common(k)]
print(top_k([1,1,1,2,2,3],2))
'''

