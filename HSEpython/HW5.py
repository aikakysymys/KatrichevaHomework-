import os
import re


def get_max_depth(path, x=0):
    if not os.path.isdir(path):
        return x
    maxdepth = x
    for entry in os.listdir(path):
        fullpath = os.path.join(path, entry)
        maxdepth = max(maxdepth, get_max_depth(fullpath, x + 1))
    return maxdepth


# находим количество папок с полностью кириллическими названиями
def cyrillic_dirs(path):
    count = 0
    cyrillic = u'[а-яёА-ЯЁ]'
    for root, dirs, files in os.walk(path):
        for name in dirs:
            if re.search(cyrillic, name):
                count += 1
    num = '\n2. Количество папок с полностью кириллическими названиями: ' + str(count)
    return num


#находит наиболее частотное расширение
def freq_ext(path):
    extensions = []
    for root, dirs, files in os.walk(path):
        for name in files:
            sep = '.'
            ext = name.split(sep, -1)[-1]
            extensions.append(ext)
    keys = set(extensions)
    ext_frequencies = dict.fromkeys(keys, 0)
    for e in extensions:
        if e in ext_frequencies:  # проверяет ключ
            ext_frequencies[e] += 1
        else:
            ext_frequencies[e] = 1
    extention = '\n3. Наиболее частотное расширение: .' \
    + max(ext_frequencies, key=ext_frequencies.get)
    return extention


#находим наиболее частотную букву в названии папки
def freq_first_l(path):
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
        if l in l_frequency:
            l_frequency[l] += 1
        else:
            l_frequency[l] = 1
    letter = '\n4. Наиболее частотная первая буква в названии папки: ' + max(l_frequency, key=l_frequency.get)
    return letter


#находим количество файлов с разными названиями с учётом расширений
def diff_names_ext(path):
    f_names = []
    for root, dirs, files in os.walk(path):
        for name in files:
            f_names.append(name)
    count = len(set(f_names))
    num = '\n5.1. Количество файлов с разными названиями с учётом расширений: ' + str(count)
    return num


#находим количество файлов с разными названиями без учёта расширений
def diff_names_no_ext(path):
    f_names = []
    for root, dirs, files in os.walk(path):
        for name in files:
            sep = '.'
            ext = name.split(sep, -1)[-1]
            bits = name.split('.')
            if ext in bits:
                bits.remove(ext)
            clean_name = ''.join(bits)
            f_names.append(clean_name)
    count = len(set(f_names))
    num = '\n5.2. Количество файлов с разными названиями без учёта расширений: ' + str(count)
    return num


#в скольких папках встречается несколько файлов с одним и тем же расширением
def dirs_same_file_ext(path):
    extensions = []
    same_file_ext = 0
    for root, dirs, files in os.walk(path):
        for name in files:
            sep = '.'
            ext = name.split(sep, -1)[-1]
            extensions.append(ext)
        if len(extensions) > len(set(extensions)):
            same_file_ext += 1
        extensions = []
    extention = '\n6. Количество папок, где более одного файла с определённым расширением: ' \
                + str(same_file_ext)
    return extention


#находим наибольшее количество файлов в папке
def more_files(path):
    max_num = 0
    count = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            count += 1
        if count > max_num:
            max_num = count
        count = 0
    max_num = '\n7. Наибольшее количество файлов в папке: ' + str(max_num)
    return max_num


# собираем всю информацию в одну переменную
def all_output():
    start_path = os.getcwd()
    x = 0
    output = "1. Наибольшая глубина папки: " + str(get_max_depth(start_path)) +\
             cyrillic_dirs(start_path) + freq_ext(start_path) + freq_first_l(start_path) +\
             diff_names_ext(start_path) + diff_names_no_ext(start_path) + \
             dirs_same_file_ext(start_path) + more_files(start_path)
    return output


def main():
    f = open('folder_info.txt', 'w')
    s = all_output()
    f.write(s)
    f.close()
    return 0


if __name__ == '__main__':
    main()
