import math


def square(side):
    area = side ** 2
    if isinstance(side, int):
        return area
    return math.ceil(area)

print(square(4))
print(square(4.5))
