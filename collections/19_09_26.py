s={1,2,3}
s.add(4)
s.add(2)
s.update([5,6])
print(s)
s.remove(6)
s.discard(99)
print(hash(5))
x=s.pop()       #here we cant pop using index becz sets has no indexing
s.clear()
print(s)

a={1,2,3,4}
b={3,4,5,6}

#we knew that sets is a math topic

print(a.union(b))
print(a|b)

print(a.intersection(b))
print(a&b)

print(a-b) #in a,not in b

print(a^b)  #opposite to intersection

print({1,2}.issubset({1,2,3}))
print({1,2,3}.issuperset({1,2}))
print({1,2}.isdisjoint({3,4}))

#frozenset

squares={x*x for x in range(-3,4)}
print(squares)
vowels_in={c for c in "consistency" if c in "aeiou"}
print(vowels_in)

big_list=list(range(1_000_000))
big_set=set(big_list)
print(999_999 in big_list)    #o(n)
print(999_999 in big_set)     #o(1)

def first_duplicate(nums):
    seen=set(nums)
    a=set()
    for i in nums:
        if nums.count(i)>1:
            a.add(i)
    return a
print(first_duplicate([1,2,3,4,5]))

def dedup_ordered(nums):
    seen=set()
    out=[]
    for x in nums:
        if x not in seen:
            seen.add(x)
            out.append(x)
    return out
print(dedup_ordered([3,1,3,2,1,4]))

def intersect_union(a,b):
    sa,sb=set(a),set(b)
    return sorted(sa & sb),sorted(sa|sb)
common,combined=intersect_union([1,2,2,3],[2,3,4])
print(common)
print(combined)

from collections import Counter
def is_anagram(a,b):
    return Counter(a)==Counter(b)
print(is_anagram("listen","silent"))
print(is_anagram("aab","abb"))

#Dictionaries

