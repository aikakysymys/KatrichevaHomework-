sent = input()
l = sent.lower()
words = l.split()
for i in words:
    i = i.strip('!.?,:;')
    if len(i) > 5:
        print(i)
