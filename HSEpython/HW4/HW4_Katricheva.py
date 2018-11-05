import re


def shashlik():
    file = "wiki_li_hw4.txt"
    with open(file) as f, open('wiki_sh_hw4.txt', 'w') as w:
        lines = f.readlines()
        for line in lines:
            if re.search('язык|Язык', line):
                line = re.sub(r'язык(.{0,2}и?[\W])', r'шашлык\1', line)
                line = re.sub(r'Язык(.{0,2}и?[\W])', r'Шашлык\1', line)
            w.write("%s\n" % line)


def malaysia():
    file = "wiki_fi_hw4.txt"
    with open(file) as f, open('wiki_ma_hw4.txt', 'w') as w:
        lines = f.readlines()
        for line in lines:
            if re.search('ФИНЛЯНДИ|финлянди|Финлянди|Финля́нди', line):
                line = re.sub(r'финл.{2,3}ди([а-я]{1,2}[\W])', r'Малайзи\1', line)
                line = re.sub(r'Финл.{2,3}ди([а-я]{1,2}[\W])', r'Малайзи\1', line)
                line = re.sub(r'ФИНЛ.{2,3}ДИ([А-Я]{1,2}[\W])', r'МАЛАЙЗИ\1', line)
            w.write("%s\n" % line)


def astrology():
    file = "wiki_phi_hw4.txt"
    with open(file) as f, open('wiki_ast_hw4.txt', 'w') as w:
        lines = f.readlines()
        for line in lines:
            if re.search('ФИЛОСОФИ|философи|Философи|Филосо́фи', line):
                line = re.sub(r'философи([а-я]{1,2}[\W])', r'астрологи\1', line)
                line = re.sub(r'Филос.{2,3}и([а-я]{1,2}[\W])', r'Астрологи\1', line)
                line = re.sub(r'ФИЛОС.{2,3}И([А-Я]{1,2}[\W])', r'АСТРОЛОГИ\1', line)
            w.write("%s\n" % line)


def main():
    shashlik()
    malaysia()
    astrology()
    return 0


if __name__ == '__main__':
    main()
    