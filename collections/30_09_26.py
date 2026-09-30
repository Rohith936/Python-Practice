#kargs
#is used acceptnany number of keyword arguments
'''
def my_function(**myvar):
  print('Type:',type(myvar))
  print('Name:',myvar['name'])
  print('Age:',myvar['age'])
  print('All data:',myvar)
my_function(name='Tobias',age=30,city='Bergen')

def my_function(username,**details):
  print('Username:',username)
  print('Additional details:')
  for key,value in details.items():
    print(' ',key+':',value)
my_function("emil123", age = 25, city = "Oslo", hobby = "coding")

def my_function(title,*args,**kwargs):
  print('Title:',title)
  print('Positional arguments:',args)
  print('Keyword arguments:',kwargs)
my_function("User Info", "Emil", "Tobias", age = 25, city = "Oslo")

def my_function(a,b,c):#unpacking a list
  return a+b+c
numbers=[1,2,3]
print(my_function(*numbers))

def my_function(fname,lname):
  print('Hello',fname,lname)
person={'fname':'Emil','lname':'Refsnes'}
my_function(**person)

def myfunc():
  x=300
  print(x)
myfunc()

def myfunc():
  x=300
  def myinnerfunc():
    print(x)
  myinnerfunc()
myfunc()
'''
