'''
def my_fun(*kids):
    print('The youngest child is '+kids[2])

my_fun('Emil','Tobias','Linus')

def my_function(a, b, /, *, c, d):
  return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result)

def my_function(*args):
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)
my_function('Emil','Tobias','Linus')

def my_fun(greeting,*names):
  for name in names:
    print(greeting,name)
my_fun("Hello", "Emil", "Tobias", "Linus")

def my_fun(*numbers):
  total=0
  for num in numbers:
    total+=num
  print(total)
my_fun(1,2,3)
my_fun(10,20,30,40,50)

i=['a','f','g']
for j in i:
    print(j)
'''
target='f'
print(ord(target))
