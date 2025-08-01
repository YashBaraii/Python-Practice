# Use reduce() to compute GCD of a list of numbers

from functools import reduce
from math import gcd

lst = [12, 18, 66, 24]

greatest_common_divisor = reduce(lambda x, y: gcd(x, y), lst)

print("The GCD among above list is: ", greatest_common_divisor)
