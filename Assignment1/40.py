tuple1 = (2, 4, 6, 8, 10)
print(tuple1)
tuple1 = tuple1 + (11,)
print(tuple1)
tuple1 = tuple1[:5] + (15, 20, 25) + tuple1[:5]
print(tuple1)
list1 = list(tuple1)
list1.append(30)
tuple1 = tuple(list1)
print(tuple1)