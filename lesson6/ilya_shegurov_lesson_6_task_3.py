import pandas as pd


users = []
users_hobby = []
data_of_hobbies = {}

with open('users.csv', encoding='utf-8') as f_1:
    with open('hobby.csv', 'r', encoding='utf-8') as f_2:
        for hobbies, user in zip(f_2, f_1):
            user = ' '.join(user.split(',')).strip().join(" :")

            data_of_hobbies[user] = hobbies

df = pd.DataFrame.from_dict(data_of_hobbies, orient ='index')
print(df)
