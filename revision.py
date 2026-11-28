#local and global variables
'''
message="I am global"
def show():
    greeting="I am local"
    print(message)
    print(greeting)
show()
print(message)

count=0
def increment_wrong():
    count+=1
def increment_right():
    global count
    count=count+1
increment_right()
print(count)
'''
