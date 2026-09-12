def p22(n=5):
    for i in range(1,n+1):
        left=''
        right=''
        for j in range(i):
            left+=''.join(chr(65+j))
        for j in range(i-1,0,-1):
            right+=''.join(chr(64+j))
        print(' '*(n-i)+left+right)
p22()



def p_22(n=5):
    for i in range(1,n+1):
        left=''.join(chr(64+j) for j in range(1,i+1))
        right=''.join(chr(64+j) for j in range(i-1,0,-1))
        print(' '*(n-i)+left+right)
p_22()
