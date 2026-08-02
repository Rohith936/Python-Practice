nu = "582947"
print(f"Digit:{nu[2:]}")
print(f"Digit:{nu[:2]}")
num = 582947
print("Digit 1:",int((num//10e4)))
a=(num//10e3)
print("Digit 2:",int((a%10)))
b=(num//10e2)
print("Digit 3:",int((b%10)))
c=(num//10e1)
print("Digit 4:",int((c%10)))
d=(num//10)
print("Digit 5:",int((d%10)))
print("Digit 6:",(num%10))

