'''
def my_generator():
  yield 1
  yield 2
  yield g
for i in my_generator():
  print(i)
  
def count_n(n):
  count=1
  while count<=n:
    yield count
    count+=1
for num in count_n(9):
  print(num)

def large_sequence(n):
  for i in range(n):
    yield i
gen=large_sequence(1000000)
print(next(gen))
print(next(gen))
print(next(gen))

list_comp=[x*x for x in range(5)]
print(list_comp)
gen_exp=(x*x for x in range(5))
print(gen_exp)
print(list(gen_exp))

def fibnacci():
  a,b=0,1
  while True:
    yield a
    a,b=b,a+b
gen=fibnacci()
for _ in range(100):
  print(next(gen))

def my_gen():
  try:
    yield 1
    yield 2
    yield 3
  finally:
    print("Generator closed")
gen=my_gen()
print(next(gen))
gen.close()

def echo_generator():
  while True:
    received=yield
    print('Received:',received)
gen=echo_generator()
next(gen)
gen.send('Hello')
gen.send('World')
'''
