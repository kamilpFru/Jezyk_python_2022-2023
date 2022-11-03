import string

zdanie = 'In Python 27 and 3 you can use this'.lower()
ilosc_slow = len(zdanie.split())
ilosc_cyfr = sum(i.isdigit() for i in zdanie)
ilosc_liter = sum(i.isalpha() for i in zdanie)
czestotliwosc = {}

for i in zdanie:
    if i in czestotliwosc:
        czestotliwosc[i] += 1
    else:
        czestotliwosc[i] = 1

print('\n', 'Slowa: ', ilosc_slow, '\n', 'Litery: ', ilosc_liter, '\n', 'Cyfry: ', ilosc_cyfr, '\n', sep='')
print(str(czestotliwosc))

