import os

''' script which makes folders structure'''


def create_main_dir(dir_name):
    try:
        os.path.exists(dir_name)
        os.mkdir(dir_name)
    except FileExistsError as e:
        print(f'dir exist; {e.filename}')
        return 0


def create_child_dirs(parent, *dirs):
    for el in dirs:
        try:
            dir_in_main = parent, el
            dir_path = os.path.join(*dir_in_main)
            os.path.exists(dir_path)
            os.mkdir(dir_path)
        except FileExistsError as e:
            print(f'dir exist:{e.filename}')
            return 0


def create_starter(main_dir):
    create_main_dir(main_dir)
    create_child_dirs(main_dir, 'settings', 'mainapp', 'adminapp', 'authapp')


if __name__ == '__main__':
    create_starter('my_project4')
