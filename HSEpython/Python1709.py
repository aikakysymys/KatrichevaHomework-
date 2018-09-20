s = 'love love'
l = s.split() # ' ' в качестве разделителя
k = list(s)
print(l)
print(k)

words = text.split()
for word in words: # здесь word берётся из изначального списка, "ничего не меняется
    word = word.strip('!.?,:;')
    l.append(word) # а тут вроде! формируется новый словарь
# список меняется во всех своих ипостасях - как перезаписать список?

for i in enumerate(words):
    words[i] = word.strip(',')

l = [] # нормальный способ создать список
l = l.append()
l = s.split()

s1 = ' '.join(l) # join list elements into a string

l1 = [1, 2, 3]
l2 = [4, 5]
l1.append(l2) # [1, 2, 3, [4, 5]]
l1.extend(l2)

# ключи словаря - неизменяемые типы данных: str, int, float,
# а list и dict не могут
# ключ должен быть уникальным

# а значением list и dict быть могут

d = {}
d[1] = 'a'
d['abc'] = 5 # можно хранить
# информацию про слова, частотный словарь, например

d = {}
text = '...'
words = text.split()
for word in words:
    if word in d: # проверяет ключ
        d[word] += 1 # ключ - это переменная word, прибавляем 1 к значению
    else:
        d[word] = 1

for word in d:
    print(word)
    print(d[word])

trans = {'а':'a',
         'б':'b'} # кирилл и латин

word = input()
for letter in word:
    if letter in trans:
        print(trans[letter])

d[1] = [] # список лежит в значении словаря
d[1].append(sth)

d = {1:'a'
     2:{'a':'abc'}
     }

s1 = d[2]['a'] # достать 'abc'

l = [x for x in range(100) if x $ 2 == 0]
l = [x for x in range(100)]

d = {x:0 for x in 'abc'} # ключи буквы а б и с, а значения нули

for x in sorted(d): # алфавитная сортировка по ключам, а по значениям не сортируют обычно
    print(x)
    print(d[x])

d = {'a':1....}
keys_list = list(d.keys())
val_list = list(d.valuse())

set() #  нельзя менятьб инднемов нет, но легко! посчитать уникальные элементы
s = set(['a', 'a', 'b', 'c'])
len(s)

a1 = set(a)
a2 = set(b)
amp = a1 & a2 # пересечение множеств
raz = a1 - a2
l = list(amp)

a = [1, 2, 3]
b = a[1:] # делаем копию всего списка
c = a[:-1]
d = a[::-1] # в обратную сторону список

different!!!
d = a[:] --- d = a



