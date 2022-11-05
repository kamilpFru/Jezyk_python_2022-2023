import json
with open('tramwaje.json', "r", encoding='utf-8') as read_file:
    data = json.load(read_file)

y = data['linia']

trams = {}
liczba_przystankow = {}
zbior_przystankow = set()

for i in range(len(y)):
    nr_linii = y[i]['name']
    lista = []
    if 'przystanek' in y[i]:
        for j in range(len(y[i]['przystanek'])):
            nazwa_przystanku = y[i]['przystanek'][j]['name'][:-3]
            lista.append(nazwa_przystanku)
            zbior_przystankow.add(nazwa_przystanku)
        liczba_przystankow[nr_linii] = len(y[i]['przystanek'])
    else:
        liczba_przystankow[nr_linii] = 0

    trams[nr_linii] = tuple(lista)

przystanki = dict(sorted(liczba_przystankow.items(), key=lambda x: x[1], reverse=True))

for key, value in przystanki.items():
    print(key, ' - ', value)

with open('tramwaje_out.json', 'w', encoding='utf-8') as file:
   json.dump(trams, file, ensure_ascii=False)

print(sorted(zbior_przystankow))