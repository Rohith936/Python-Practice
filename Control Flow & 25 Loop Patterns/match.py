day=4
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")

status=int(input("Enter number:"))
def http(status):
    match status:
        case 200:
            return "OK"
        case 301 | 302:
            return "Redirect"
        case code if code >= 500:
            return "Service error"
        case _:
            return "Other"
print(http(status))
    
    

