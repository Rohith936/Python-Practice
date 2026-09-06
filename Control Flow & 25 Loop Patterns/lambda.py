words = ["apple", "hi", "banana", "cat"]
words.sort(key=lambda words: len(words))
print(words)

#w or words itself our wish

words = ["apple", "hi", "banana", "cat"]
words.sort(key=lambda w: len(w))
print(words)


add=lambda a,b:a+b*a-b
print(add(4,8))

a=list(map(int,input("Enter digits into list:").split(',')))
maxi=lambda a:max(a)
print(maxi(a))    


