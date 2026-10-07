from array import array
a=array('i',[10,20,30])
a.append(40)
print(a,a.typecode,a[0])

class Countdown:
  def __init__(self,start):
    self.n=start
  def __iter__(self):
    return self
  def __next__(self):
    if self.n <=0:
      raise StopIteration
    self.n -= 1
    return self.n + 1
print(list(Countdown(5)))

stock = {"apples": 34, "bananas": 12, "oranges": 57, "grapes": 8, "mangoes": 23}
b=min(stock.values())
for k in stock.keys():
  if stock[k]==b:
    print(k)

#1
from array import array
a=array('i',[10,20,30])
a.append(40)
b=a.pop(0)
print(list(a),b)
#2
nums=[4,9,2,7]
m=nums[0]
for x in nums[1:]:
  if x>m:
    m=x
print(m)
