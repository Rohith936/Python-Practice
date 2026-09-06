def total(*nums):
    return sum(nums)
print(total(2,3,5,1,4,5,2))
print(total(10.543232,63.987654))


def tota(*nums):
    return round(sum(nums),2)
print(tota(2,3,5,1,4,5,2))
print(tota(10.543232,63.987654))


def sum1(*nums, **opts):
    return round(sum(nums), opts.get("digits", 2))
print(sum1(10.5432, 20.1234))
print(sum1(10.5432, 20.1234, digits=3))
print(sum1(10.5432, 20.1234,6,3,"res"))


#if we want to take total set at atime "*nums"
#if we want to take user input "**opts"
