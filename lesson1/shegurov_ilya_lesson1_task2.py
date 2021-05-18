my_cube_list = []
finished_number = 1000
number = 0
while number < finished_number:
    my_cube_list.append(number ** 3 // 7 + 17)
    number += 1
print(my_cube_list)
