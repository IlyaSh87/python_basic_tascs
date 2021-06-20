tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Станислав', 'Владимир'
]

klasses = [ '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


def shcool_staff(tutors, klasses):
    _tutors = (el for el in tutors)
    _klasses = (el for el in klasses)
    for school in zip(_klasses, _tutors):
        yield school[::-1]
    for rest in _tutors:
        yield rest, None

student = shcool_staff(tutors, klasses)
print(type((student)))
print(next(student))
print(next(student))
print(next(student))
print(next(student))
print(next(student))
print(next(student))
print(next(student))
print(next(student))
print(next(student))
print(next(student))
print(next(student))
