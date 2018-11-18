import os
import re


# находим максимальную глубину дерева
def get_max_depth(path, x=0):
    if not os.path.isdir(path):
        return x
    maxdepth = x
    for entry in os.listdir(path):
        fullpath = os.path.join(path, entry)
        maxdepth = max(maxdepth, get_max_depth(fullpath, x + 1))
    return maxdepth


def cyrillic_dirs(path):
    count = 0
    cyrillic = u'[а-яёА-ЯЁ]'
    for root, dirs, files in os.walk(path):
        for name in dirs:
            if re.search(cyrillic, name):
                count += 1

    num = '\nКоличество папок с кириллическими названиями: ' + str(count)
    return num

 #  filename, file_extension = os.path.splitext(path)


def freq_txt(path):
    count = 0
    for root, dirs, files in os.walk(myPath):
        for file in files:
            if file.endswith('.txt'):
                count += 1

    return str(count)


def freq_first_l(path):
    l_name = []
    first_l = []
    cyrillic = u'[а-яёА-ЯЁa-zA-Z]'
    for root, dirs, files in os.walk(path):
        for name in dirs:
            l_name = list(name)
            if re.search(l_name[0], cyrillic):
                first_l.append(l_name[0])
    keys = set(first_l)
    l_frequency = dict.fromkeys(keys, 0)
    for l in first_l:
        if l in l_frequency:  # проверяет ключ
            l_frequency[l] += 1
        else:
            l_frequency[l] = 1
    letter = '\nНаиболее частотная первая буква: ' + max(l_frequency, key=l_frequency.get)
    return letter


def diff_names(path):
    f_names = []
    for root, dirs, files in os.walk(path):
        for name in files:
            f_names.append(name)
    count = len(set(f_names))
    num = '\nКоличество файлов с разными названиями: ' + str(count)
    return num


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
    max_num = '\n7. Наибольшее количество файлов в папке: ' + str(max_num)
    return max_num


def max_length():
    start_path = '.'
    for root, dirs, files in os.walk(start_path):
        print('Где мы сейчас:', root)
        print('Папки на этом уровне:', dirs)
        print('Файлы на этом уровне:', files)
    return



def all_output():
    start_path = os.getcwd()
    x = 0
    output = "1. Наибольшая глубина папки: " + str(get_max_depth(start_path)) + cyrillic_dirs(start_path) \
             + freq_first_l(start_path) + diff_names(start_path) + more_files(start_path)
    return output


def main():
    f = open('folder_info.txt', 'w')

    start_path = os.getcwd()

    s = all_output()
    print(all_output())


    f.write(s)
    f.close()
    return 0


if __name__ == '__main__':
    main()