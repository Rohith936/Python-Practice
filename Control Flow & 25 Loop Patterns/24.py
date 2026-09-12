def p24(n=5):
    for i in range(n):
        for j in range(n):
            if j==i or i+j==n-1: #or j == n-1-i
                print('*',end='')
            else:
                print(' ',end='')
        print()
p24()



                
