#ASCII
print(ord('A'))       #from alphabet to value
for i in range(65,90):    #from value to aplphabet
    print(chr(i))



def p_21(n=5):
    for i in range(1,n+1):
        for j in range(i):
            print(chr(65+j),end=' ')
        print()

p_21()
