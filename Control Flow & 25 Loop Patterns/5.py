def p5(n=5):
    for i in range(1,n+1):
        print("  "*(n-i),"* "*i)  #1 space
p5()


def p6(n=5):
    for i in range(n, 0, -1):
        print(" " * (n-i) + "* " * i)  #2 spaces
        
p6()
