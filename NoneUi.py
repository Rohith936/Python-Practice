#NONE

x=None
print(x)
print(type(x))

result=None
if result is None:
    print('No result yet')
else:
    print('Result is ready')

result=None
if result is not None:
    print('No result yet')
else:
    print('Result is ready')

print(bool(None))
def myfunc():
    x=5
x=myfunc()
print(x)

#USER INPUT

print('Enter your name:')
name=input()
print(f"Hello {name}")
name=input('Enter your name:')
print(f"Hello {name}")

name=input('Enter your name:')
print(f"Hello {name}")
fav1=input('Fav animal:')
fav2=input('fav color:')
fav3=input('fav number:')
print(f"Do you want a {fav2} {fav1} with {fav3} legs?")

y=True
while y==True:
    x=input('Enter a number:')
    try:
        x=float(x)
        y=False
    except:
        print('Try again')
print('TQ')
