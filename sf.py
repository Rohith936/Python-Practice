#string formatting

txt=f"The price is 49 dollors"
print(txt)

price=59
txt=f"The price is {price} dollars"
print(txt)

price=59
txt=f"The price is {price:.2f} dollars"
print(txt)

price=59
tax=0.25
txt=f"The price is {price+(price*tax)} dollars"
print(txt)

price=49
txt=f"It is very {'Expensive' if price>50 else 'Cheap'}"
print(txt)

fruit='apples'
txt=f"I love {fruit.upper()}"
print(txt)

arr = list(map(int,input().split()))
t = int(input())
n = len(arr)
l= 0
r = len(arr)-1


for i in range(n):#0
    for j in range(n-i-1,-1,-1):#0-5
        s = arr[i]+arr[j]
        if s==t:
            print(arr[i],arr[j])
    break

class Car:
    pass
c1=Car()
print(c1)

def myconverter(x):
    return x*0.3048
txt=f"The plane is flying at a {myconverter(30000)} meter altitude"
print(txt)

price=590000000
txt=f"The price is {price:,} dollars"
print(txt)

