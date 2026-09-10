def p12(n=5):
    def hrow(i):
        row=''
        for j in range(1,2*i):
            row += '*' if(j==1 or j==i*2-1) else " "
        return " "*(n-i)+row
    for i in range(n,0,-1):
        print(hrow(i))
    for i in range(1,n+1):
        print(hrow(i))
p12()



def p12(n=5):
    def hrow(i):
        row=''
        for j in range(1,2*i):
            row += '*' if(j==1 or j==i*2-1) else " "
        return " "*(n-i)+row
    for i in range(1,n+1):
        print(hrow(i))
    for i in range(n-1,0,-1):
        print(hrow(i))
p12()

