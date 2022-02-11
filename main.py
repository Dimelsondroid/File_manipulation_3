import os


def _get_all_files():
    full_path = _get_path()
    all_files = tuple(os.listdir(full_path))
    return all_files


def _get_path():
    dir_path = os.getcwd()
    folder = 'tmp'
    full_path = os.path.join(dir_path, folder)
    return full_path


def file_sort(all_files=_get_all_files()):
    files_dict = {}
    for file in all_files:
        if file == 'result.txt':
            continue
        with open(os.path.join(_get_path(), file)) as text:
            length = len(text.readlines())
            files_dict[file] = length
    return files_dict


def write_file(file, length):
    with open(os.path.join(_get_path(), file)) as read:
        temp_file = read.readlines()
    with open(os.path.join(_get_path(), 'result.txt'), 'a') as save:
        save.write(file + '\n')
        save.write(str(length) + '\n')
        save.writelines(line for line in temp_file)
        save.write('\n')


def choose_file(files_dict=file_sort()):
    files_vect = sorted(files_dict.values())
    for length in files_vect:
        for key, val in files_dict.items():
            if val == length:
                write_file(key, val)


choose_file()
