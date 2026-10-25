#JSON
#1
'''
import json

#some JSON
x='{"name":"json","age":30,"city":"New York"}'

#parse x:
y=json.loads(x)

#the result is a python dictionary:
print(y['age'])
'''
#2
'''
import json

#a python object (dict):
x = {
    'name':'John',
    'age':30,
    'city':'New York'
}

#convert into JSON:
y=json.dumps(x)

#the result is a JSON string:
print(y)
'''
#3
'''
import json

print(json.dumps({'name':'Json','age':30}))
print(json.dumps(['apple','bananas']))
print(json.dumps(('apple','bananas')))
print(json.dumps('hello'))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
'''
#4
'''
import json
x={
    'name':'Json',
    'age':30,
    'married':True,
    'divorced':False,
    'children':("Ann","Billy"),
    'pets':None,
    'cars':[
        {'model':'BMW 230','mpg':27.5},
        {'model':'Ford Edge','mpg':24.1}
    ]
}
print(json.dumps(x,indent=4))
print(json.dumps(x,indent=4,separators=('.','=')))
print(json.dumps(x,indent=4,sort_keys=True))
'''
#RegEx
#5
'''
import re

text = input()  # hi my email is bhavani.m@gmail.com
pattern = r"[\w.]+@[\w.]+\.\w+"
num = r"[\d+]+"    #r is used to convert any datatype into string

emails = re.findall(pattern, text)
n = re.findall(num, text)
print(emails, n)
'''
#6
'''
import re
txt='The rain in spain'
x=re.search('^The.*spain',txt) #search to if string starts with 'The' and ends with 'spain'
print(x)
'''
# findall -> returns a list containing all matches
# search -> returns a match object if there is a match anywhere in the string
# split -> returns a list where the string has been split at each match
# sub -> replaces one or many matches with a string
#7
'''
import re
txt="The rain in Spain"
x=re.findall('[a-m]',txt)  #characters a-m in txt
print(x)
'''
#8
'''
import re
txt='The rain in spain 0987654'
x=re.findall('\d',txt) #all digits in a list
print(x)
'''
#9
'''
import re
txt='Hello rohith'
x=re.findall('He...',txt)  # it is a type of fill the blank
print(x)
'''
#10
'''
import re
txt='The rain in spain'
x=re.findall('^The',txt)
print(x)
'''
#11
'''
import re
txt='The rain in spain'
x=re.findall('spain$',txt) #matches with last word in string
print(x)
'''
#12
'''
import re
txt='The rain is spain'
x=re.findall('Th.*a',txt)
print(x)
'''
#12
'''
import re
txt='The rain is spain'
x=re.findall('Th.+a',txt)  #'+' requires at least one character in middle
print(x)
'''
#13
'''
import re
txt='The rain is spain'
x=re.findall('Th.? ',txt)   #zero or one occurences (it means 2 spaces after you mentioned)
print(x)
'''
#14
'''
import re
txt='hello is spain'
x=re.findall('he.{2}o ',txt)
print(x)
'''
#15
'''
import re
txt='The rain is spain'
x=re.findall('rain|bye',txt)
print(x)
if x:
    print('Hello')
else:
    print('Bye')
'''
#16
'''
a=int(input())
arr=[1,3,5,7,10,11,16,20,23,30,34,60]
def arr1(a,arr):
    l=len(arr)//2-1
    for i in range(len(arr)):
        if arr[l]==a:
            return l
        elif arr[l]<a or arr[l]>a:
            l//=2
print(arr1(a,arr))
'''
#17
'''
import re
txt="Åland"
print(re.findall('\w',txt,re.ASCII))
print(re.findall('\w',txt))
print(re.findall('\w',txt,re.A))
'''
#18
'''
import re
txt='The rain in Spain'
print(re.findall('spain',txt,re.DEBUG))
ratio=0.256
print(f"{ratio:.0%}")

def greet(name):
    """Return a friendly greeting for the given name."""
    return f"Hello, {name}!"
print(greet.__doc__) # Return a friendly greeting for the given name.
help(greet) 

a=[1,2,3,5]
print(3 in a)
a=set(a)
print(a)
print(3 in a)

print(ord('A'))
'''
#1
'''
a=input()
c=0
for i in a:
    c+=1
print(c)
'''
#2
'''
a=input()
b=''
for i in range(len(a)-1,-1,-1): 
    b+=a[i]
print(b)
'''
#3
'''
a=input()
print(a[::-1])
if a==a[::-1]:
    print('yes')
else:
    print('NO')
'''
#4
'''
a=input()
c=0
for i in a:
    if i in "aeiouAEIOU":
        c+=1
print(c)
'''
#5
'''
a=input()
b=0
c=0
for i in a:
    if ord(i)>96:
        b+=1
    else:
        c+=1
print(f'lower:{b}')
print(f'upper:{c}')
'''
#6
a='rohith'
for i in range(6-1,-2,-3):
    print(i)
