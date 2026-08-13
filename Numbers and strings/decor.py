def trans(func):

    def wrapper():
        res = func()
        print(res)
        print("before fun call")
        
        print(res**2)
        print("after fun call")

    return wrapper

@trans
def greet():
    i=int(input())
    return i%2

greet()

@trans 
def greet1():
    i=int(input())
    return i%2

greet1()
