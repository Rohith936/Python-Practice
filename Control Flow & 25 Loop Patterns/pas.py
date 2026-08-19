password=input()
le=len(password)>=8
up=any(c.isupper() for c in password)
lr=any(c.islower() for c in password)
nu=any(c.isdigit() for c in password)
if le and up and lr and nu:
    print("valid")
else:
    print("Enter valid password")
