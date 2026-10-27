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
