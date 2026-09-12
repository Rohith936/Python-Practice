def p23(n=5):
    for i in range(1,n+1):
        print('*'*i+'  '*(n-i)+'*'*i)
    for i in range(n,0,-1):
        print('*'*i+'  '*(n-i)+'*'*i)
p23()
