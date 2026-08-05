hex_val = 0x_FF_FF
print(hex_val)

a=7653
print(hex(a))

b=0x1de5
print(b)

a = 0.1 + 0.2
print(a)
print(abs(a - 0.3)<1e-9)

import math

print(math.isclose(0.1 + 0.2, 0.3))

print(True)


try:
    age = int(input("Age: "))
except ValueError:
    print("Please enter a whole number.")

