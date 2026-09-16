nums=[3,1,4,1,5,9,2]
nums.sort()
print(nums)
nums.sort(reverse=True)  #desending order
print(nums)

s=sorted(nums)    #new list
print(s)
words=["banana","kiwi","apple","fig"]
words.sort(key=len)
print(words)
words.sort(key=str.lower)
print(words)
words.reverse()
print(words)
words.sort(key=str.upper)
print(words)


people=[("Asha",30),("Ravi",25),("Asha",22)]
people.sort(key=lambda t: (t[0],t[1]))   #name acending then age will be considerd
print(people)

students=[('A',85),('B',90),('C',85)]
students.sort(key=lambda s: (s[1],s[0]))    #age acending then name is considered
print(students)

students=[('A',85),('B',90),('C',85)]
students.sort(key=lambda s: (-s[1],s[0]))    #age desending then name is considered
print(students)

# in lambda functions we consider the items in list it may be string/number/tuple

