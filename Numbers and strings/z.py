a="Hello world"
print(f"Reverse of a:{a[::-1]}")
b=a.split(' ')
x,y=b
print(f"Reverse of words in a:{x[::-1]} {y[::-1]}")
e=' '.join([x[::-1],y[::-1]]) #we need to give in '[]'
print(f"Reverse of words in a:{e}")
