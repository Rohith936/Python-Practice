class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        s=''
        for i in num:
            s+=str(i)
        a=str(int(s)+k)
        b=[]
        for i in a:
            b.append(int(i))
        return b
