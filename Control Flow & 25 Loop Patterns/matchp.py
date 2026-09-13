def area(shape):
    match shape:
        case ("circle",a):
            return 3.14*a*a
        case ("square",a):
            return a*a
        case ("rectangle",l,w):
            return l*w
print(area(("circle",2)))
