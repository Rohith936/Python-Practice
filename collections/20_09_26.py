s = "A man, a plan, a canal: Panama"
s=s.lower()
i=0
j=len(s)-1
while i<j:
    if s[i].isalnum()==False and s[j].isalnum()==True:
        i+=1
    elif s[i].isalnum()==True and s[j].isalnum()==False:
        j-=1
    elif s[i].isalnum()==False and s[j].isalnum()==False:
        i+=1
        j-=1
    else:
        print(s[i]==s[j])
        j-=1
        i+=1
        
d={'name':'Asha','score':92}
print(d)
e=dict(name='Asha',score=92)
print(e)
f=dict([('a',1),('b',2)])
print(f)
g=dict(zip(['a','b','c'],[1,2,3]))  #compining two lists
print(g)
h=dict.fromkeys(['x','y','z'],0)  #{'x':0,'y':0,'z':0}
print(h)
comp={k:k*k for k in range(4)}
print(comp)


#read
d={'name':'Asha','score':92}
d['name']   #asha
print(d.get('age'))
print(d.get('age',0))
print('score' in d)
print(d)

#create/update
di={'a':1}
di['b']=2
di['a']=99
print(di)
di.update({'c':3,'a':100})
di.setdefault('d',4)
di.setdefault('a',0)  #dont change th e value of a a=100

#delete
dic={'a':1,'b':2,'c':3,'d':4}
del dic['a']
print(dic)
v=dic.pop('b')      #removes element using key
print(dic)
k,v=dic.popitem()   #removes and return the last inserted pair
print(dic)
dic.clear()
print(dic)
