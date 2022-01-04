from functools import reduce
l = [3,6,5,4,2,1,7,8,345]
a = reduce(max, l)
print(a)