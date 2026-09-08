def p1(n=5):
    for i in range(n):
        for j in range(n):
            print("*",end=' ')
        print()
p1()





n=int(input("Enter a digit:"))
def p_1(n):
    result=''
    for i in range(n):
        for j in range(n):
            result+='* '
        result+='\n'
    return result
print(p_1(n))





for i in range(5):
    for j in range(5):
        print('*',end=' ')
    print()
        
