lst=[1,2,3,4,5]
lst.extend([6,7])
print(lst)
lst[0]=99   #to replace
print(lst)
lst[1:3]=[20,30,40]  #slice assignment can change length!
print(lst)
lst[::2]=[0,0,0,0]   #change alternative
print(lst)  
print(lst[::-1])
