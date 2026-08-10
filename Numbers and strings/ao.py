user=input("Enter username:")
pwd=input("Enter password:")
is_admin=input("Enter admin username:")
if((user and pwd) or is_admin):
    print("Login is successful")
else:
    print("Cant login")
