import re


def prepare_file():
    file = "China.tsv"
    with open(file) as f:
        lines = f.read()
        words = lines.split(' ')
        for i, word in enumerate(words):
            words[i] = word.strip('.,?:(; )\\n')
            words[i] = re.sub('\\n.*', '', words[i])
            for i, word in enumerate(words):
                words[i] = word.strip('.')
    return words


def extract_objects(words):
    s = words
    i = 0
    for s[i] in s:
        if re.search('«[АВ-ЛН-ЯЁав-лн-яё]*(|-[0-9]{1,2})?»', s[i]):
            t = []
            t.append(s[i])
            print(' '.join(t))
        i += 1

    return


def main():
    s = extract_objects(prepare_file())
    return s


if __name__ == '__main__':
    main()
