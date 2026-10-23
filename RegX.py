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
