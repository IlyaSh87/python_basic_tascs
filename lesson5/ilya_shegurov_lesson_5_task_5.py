src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]


nums_cnt = {}
for num in src:
    if num not in nums_cnt:
        nums_cnt[num] = 0
    nums_cnt[num] += 1

result = [el for el in src if nums_cnt[el] == 1]
print(result)