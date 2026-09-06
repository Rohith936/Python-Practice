def min_max(xs):
    return min(xs), max(xs)
lo, hi = min_max([3, 1, 9])
print(min_max([45,23,54,765,12,43]))
print(f"min:{lo},max:{hi}")


def min_max1(*xs):
    return min(xs), max(xs)
print(min_max1(2,363,765,12,4,125,342))

#to send multiple arguments at once we use '*'
