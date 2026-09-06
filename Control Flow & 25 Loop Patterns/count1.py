count=10
def con():
    global count
    count+=1
    return count
con()
con()
con()
print(count)  #13
print(con())  #14


n=0
def c():
    n+=1
    return n
print(n)       #0
print(c())     #we will get error becz of we cant modify a local variable in a fun and to modify it we use "golobal" keyword.
    
