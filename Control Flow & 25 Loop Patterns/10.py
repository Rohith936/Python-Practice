def p10(n=5):
    for i in range(1,n+1):
        if i==1 or i==2:
            print(" "*(n-i)+'* '*i)
        elif i<n:
            print(' '*(n-i)+'* '+'  '*(i//2)+'* ')
        else:
            print('*'*(2*i-1))
p10()



def p_10(n=5):
    for i in range(1,n+1):
        rows=''
        for j in range(1,2*i):
            if j==1 or j == 2*i-1 or i == n:
                rows+='*'
            else:
                rows+=' '
        print(' '*(n-i)+rows)
p_10()
