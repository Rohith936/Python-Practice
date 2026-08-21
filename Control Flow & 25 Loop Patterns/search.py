a=list(map(int,input("Enter numbers into list:").split(',')))
while True:
    i=int(input("Enter number to search:\n")) #here we write input inside a loop.so repeatative asks for number until found
    if i not in a:
        print("Number not found")
    elif i in a:
        print("Number Found")
        break




