book = {'    ' : '\t', '\t' : '    '}
sample = '  gg    gg    '
for key in book:
    sample = sample.replace(key, book[key])
print(sample)