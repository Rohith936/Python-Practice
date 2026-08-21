a=tuple(input("Enter numbers into tuple:\n"))
print(a)
i=int(input("Enter number to search:\n"))
i=str(i)
if i not in a:
        print("Number not found")
else:
    while i:
        if i in a:
            break;
    print("Number Found")
