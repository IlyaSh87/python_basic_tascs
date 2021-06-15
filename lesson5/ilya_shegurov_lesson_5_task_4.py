src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]


src_1 = (el for el in src)
src_2 = (el for el in src)
next(src_2)
answer = (two for one, two in zip(src_1, src_2) if one < two)
print(*answer)