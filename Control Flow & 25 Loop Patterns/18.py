def p18(n=5):
    left=''
    right=''
    for i in range(1,n+1):
        for j in range(1,i+1):
            left+=str(j)
        for j in range(i-1,0,-1):
            right+=str(j)
        print(' '*(n-i)+left+right)
        left=''
        right=''
p18()



def p_18(n=5):
    for i in range(1,n+1):
        left=''.join(str(x) for x in range(1,i+1))
        right=''.join(str(x) for x in range(i-1,0,-1))
        print(' '*(n-i)+left+right)
p_18()


def p__18(n=5):
    left=''
    right=''
    for i in range(1,n+1):
        for j in range(1,i+1):
            left+=''.join(str(j))
        for j in range(i-1,0,-1):
            right+=''.join(str(j))
        print(' '*(n-i)+left+right)
        left=''
        right=''
p__18()


        
