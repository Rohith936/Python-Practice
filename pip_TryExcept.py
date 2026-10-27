'''
a=[2,1,43,12,4]
print(sorted(a))

def insertionSort(arr):
    # code here
    mini=arr[0]
    for i in range(1,len(arr)):
        for j in range(i,0,-1):
            if arr[j]<arr[j-1]:
                arr[j],arr[j-1]=arr[j-1],arr[j]
            else:
                break
    return arr
print(insertionSort([5,4,3,1]))
'''
#PIP
#PIP is a package manager for python packages, or modules
#Try...Except
# try -> block lets you test a block of code for errors
# except -> block lets you handle the error
# else -> block lets you execute code when there is no error
# finally -> block lets you execute code,regardness of the result of the try- and except blocks
            # it is used to closing files after using them
            # closing database connections
            # releasing resources
            #performing actions that should happen whether an operation succeeds or fails
#1
'''        
try:
    print(x)
except:
    print('An exception occurred')
'''
#2
'''
try:
    print(x)
except NameError:
    print('Variable x is not defined')
except:
    print('Something else went wrong')
'''
#3
'''
try:
    print('Hello')
except:
    print('Something went wrong')
else:
    print('Nothing went wrong')
'''
#4
'''
try:
    print(x)
except:
    print('Something went wrong')
finally:
    print('The "try except" is finished')
'''
#5
'''
try:
    f=open('demofile.txt')
    try:
        f.write('Lorum Ipsum')
    except:
        print('Something went wrong when writing to the file')
    finally:
        f.close()
except:
    print('Something went wrong when opening the file')
'''
#6
'''
x=-1
if x<0:
    raise Exception('Sorry')
'''
#7
'''
x = "hello"
if not type(x) is int:
  raise TypeError("Only integers are allowed")
'''
