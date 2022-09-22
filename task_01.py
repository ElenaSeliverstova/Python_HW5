# Напишите программу, удаляющую из текста слова с "абв"

#1
print(' '.join(filter(lambda x: not 'абв' in x, 'Мы неабв очень любим Питон иабв Джавуабв'.split())))

#2
my_str='Мы неабв очень любим Питон иабв Джавуабв'.split()
print(' '.join(word for word in my_str if 'абв' not in word))