a=list(input("Enter characters:").split(','))
for i in a:
    print(ord(i),end=' ')


b=int(input("Starting:"))
c=int(input("Ending:"))
for i in range(b,c+1):
    print(i,chr(i))
    
    
