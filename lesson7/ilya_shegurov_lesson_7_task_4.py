import os


def show_stat(folder_path):
    stat = get_stat(folder_path)
    keys = list(stat)
    keys.sort()
    for key in keys:
        print(f'{key}:{stat[key]}')


def get_stat(folder_path):
    stat = {}
    for root, some_data, files in os.walk(folder_path):
        for file in files:
            size = os.stat(os.path.join(root, file)).st_size
            if size <= 100:
                key = 100
            elif size <= 1000:
                key = 1000
            elif size <= 10000:
                key = 10000
            if not stat:
                raise Exception('В директории нет файлов')
            return stat


if __name__ == '__main__':
    try:
        my_folder_path = './'
        show_stat(my_folder_path)
    except Exception as e:
        print(e)




