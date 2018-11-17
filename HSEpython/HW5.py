import os
import re


# находим максимальную глубину дерева
def get_depth(path, x=0):
    if not os.path.isdir(path):
        return x
    maxdepth = x
    for entry in os.listdir(path):
     fullpath = os.path.join(path, entry)
     maxdepth = max(maxdepth, get_depth(fullpath, x + 1))
    return maxdepth


def cyrillic_dirs(path):
    count = 0
    cyrillic = u'[а-яёА-ЯЁ]'
    for root, dirs, files in os.walk(path):
        for name in dirs:
            if re.search(cyrillic, name):
                count += 1
                print(name)
    return count

 #  filename, file_extension = os.path.splitext(path)

def freq_txt(path):
    count = 0
    for root, dirs, files in os.walk(myPath):
        for file in files:
            if file.endswith('.txt'):
                count += 1
    return count


def freq_first_l(path):
    l_name = []
    first_l = []
    for root, dirs, files in os.walk(path):
        for name in dirs:
            l_name = list(name)
            first_l.append(l_name[0])
    keys = set(first_l)
    l_frequency = dict.fromkeys(keys, 0)
    for l in first_l:
        if l in l_frequency:  # проверяет ключ
            l_frequency[l] += 1
        else:
            l_frequency[l] = 1
    letter = max(l_frequency, key=l_frequency.get)
    return letter


def diff_names(path):
    f_names = []
    for root, dirs, files in os.walk(path):
        for name in files:
            f_names.append(name)
    count = len(set(f_names))
    return count


def more_files(path):
    max_num = 0
    count = 0
    if not os.path.isdir(path):
        return x
    for root, dirs, files in os.walk(path):
        for file in root, dirs:
            count += 1
        if count > max_num:
            max_num = count
    return max_num

def max_length():
    start_path = '.'
    for root, dirs, files in os.walk(start_path):
        print('Где мы сейчас:', root)
        print('Папки на этом уровне:', dirs)
        print('Файлы на этом уровне:', files)
    return



def main():
    f = open('folder_info.txt', 'w')

    start_path = os.getcwd()
    x = 0
    print(get_depth(start_path, x))

    print(cyrillic_dirs(start_path))


    print(freq_first_l(start_path))

    print(diff_names(start_path))

    print(more_files(start_path))

    s = 'Наибоьшая глубина:' +  get_depth(start_path, x) + 'n/' + \
        'Количество папок с кириллическими названиями' + \
        cyrillic_dirs(start_path) + 'n/' + 'Наиболее частотная первая буква' + \
        freq_first_l(start_path) + 'n/' + 'Количество файлов с разными названиями' \
        + diff_names(start_path) + 'n/' + 'Наибольшее количество файлов в папке' + \
        more_files(start_path)
    f.write(s)
    f.close()
    return 0


if __name__ == '__main__':
    main()