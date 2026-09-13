op=input("Enter operator:")
a=int(input("a:"))
b=int(input("b:"))
def cal(op,a,b):
    match op:
        case '+':
            return a+b
        case '-':
            return a-b
        case '*':
            return a*b
        case '/':
            return a/b
        case '%':
            return a%b
        case '//':
            return a//b
        case _:
            return f"Enter correct operator"
print(cal(op,a,b))
        
