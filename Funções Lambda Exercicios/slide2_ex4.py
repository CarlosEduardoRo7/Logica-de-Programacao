from functools import reduce

valores = [1, 2, 3, 4, 5]
multi = reduce(lambda x,y: x*y, valores)

print(multi)