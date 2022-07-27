# 1- Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# 'абвгдейка - это передача' = >" - это передача"

s = 'абвгдейка - это передача'
filter_ = 'абв'

def filter_text(text):
    text = text.split(' ')
    func = lambda word: 'абв' not in word
    return ' '.join(list(filter(func, text)))

print(filter_text(s))
