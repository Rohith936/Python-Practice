'''
l1=[1,2,3]
l2=[3,4,5]
a=int(''.join(map(str,l1)))#123 -> means joining the list items and converting into integer 
b=int(''.join(map(str,l2)))
result=str(a+b)
print(list(map(int,result)))#converting lists




c=[1,2,3]
result=''.join(map(str,c))#123 -> means joining the list items
print(result)
print(type(result))



def nu(num):
    a=0
    while num:
        if num%2==0:
            num/=2
        else:
            num-=1
        a+=1
    return a
print(nu(17))




nums=[12,324,1234]
a=len(nums)-1
d=0
while a>=0:
    c=nums[a]
    b=0
    while c:
        c//=10
        b+=1
    a-=1
    if b%2==0:
        d+=1
print(d)



n=234
n=list(str(n))
a=len(n)-1
b=1
c=0
while a>=0:
    b*=int(n[a])
    c+=int(n[a])
    a-=1
print(b-c)





candies = [2,3,5,1,3]
extraCandies=3
a=len(candies)
b=[]
for i in range(a):
    c=candies[i]+extraCandies
    b.append(c)
d=min(b)
for i in range(a):
    if b[i]==d:
        b[i]=False
    else:
        b[i]=True
print(b)


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

'''  
'''
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        return list(set(nums1).intersection(set(nums2)))
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        num=sorted(nums1+nums2)
        if len(num)%2!=0:
            return num[len(num)//2]
        else:
            return (num[len(num)//2]+num[(len(num)//2)-1])/2
'''
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in nums:
            if i==0:
                nums.remove(i)
                nums.append(i)
                
class Solution:
    def isHappy(self, n: int) -> bool:
        b=[]
        while n:
            a=0
            b.append(n)
            for i in str(n):
                a+=int(i)**2
            if a==1:
                return True
            if a in b:
                return False
            n=a
class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        a=[]
        c=0
        for i in nums:
            c+=i
            a.append(c)
        return a
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        a=[]
        b=0
        c=len(nums)//2
        for i in range(len(nums)//2):
            a.append(nums[b])
            a.append(nums[c])
            b+=1
            c+=1
        return a
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a=len(nums)
        nums.reverse()
        k=k%a
        nums[:k]=nums[:k][::-1]
        nums[k:]=nums[k:][::-1]
class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        a=[]
        for i in accounts:
            a.append(sum(i))
        return max(a)
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a,b=int(a,2),int(b,2)
        return str(bin(a+b)[2:])
