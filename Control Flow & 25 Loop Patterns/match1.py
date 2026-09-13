day=4
match day:
    case 1|2|3|4|5:
        print("Today is a weekday")
    case 6|7:
        print("I love weekends!")
    case _:
        print("No match")


point=tuple(map(int,input().split(',')))
def describe(point):
    match point:
        case (0,0):
            return "origin"
        case (0,y):
            return f"on y-axis at {y}"
        case (x,0):
            return f"on x-axis at {x}"
        case (x,y):
            return f"on ({x},{y})"
print(describe(point))
            
