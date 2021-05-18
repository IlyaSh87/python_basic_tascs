temp_s = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_temp = []
for el in temp_s:
    if el.isdigit():
        num = int(el)
        new_temp.extend(["'", f'{num:02d}', "'"])
    elif el.startswith('-') and el[1:].isdigit() or\
        el.startswith('+') and el[1:].isdigit():
        num = int(el[1:])
        new_temp.extend(["'", f'{el[0]} {num:02d}', "'"])
    else:
        new_temp.append(el)
    new_temp.append(' ')
    temp = ''.join(new_temp).strip()
print(new_temp)
print(temp)

