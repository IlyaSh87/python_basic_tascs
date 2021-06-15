def odd_num(n):
    for num in range(1, n + 1, 2):
        yield num


odd_to_15 = odd_num(15)
print(next(odd_to_15))