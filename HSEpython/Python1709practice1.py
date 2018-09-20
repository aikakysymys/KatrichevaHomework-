sent = input()
l = sent.lower()
words = l.split()
for i in words:
    i = i.strip('!.?,:;')

trans = {'ა':'а',
         'ბ':'б',
         'გ':'г',
         'დ':'д',
         'ე':'e',

}

word = input()
for letter in word:
    if letter in trans:
        print(trans[letter])

