import math
m = int(input())
bits = (((10**6)*m)*8)
qb = math.ceil(math.log2(bits))
print(qb)