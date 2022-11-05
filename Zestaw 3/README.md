# **Zestaw 3**
## **Zadanie 1**
W pliku tramwaje.json znajdują się dane z numerami linii tramwajowych w Krakowie oraz przystanków, przez
które przejeżdża dany tramwaj. W języku Python, czytanie danych w formatach .json czy .csv jest wykonywane
z pomocą modułów. W naszym przypadku:
```py
import json
with open('tramwaje.json', "r", encoding='utf-8') as read_file:
data = json.load(read_file)
```
Wczytane dane (zróbmy print) są złożone z nadmiernie zagnieżdżonych typów: słownika, listy, słownika, listy:
{'linia': [{'name': '1', 'przystanek': [{'name': 'Wzgórza Krzesławickie 01'}, {'name': 'Jarzębiny 02'} …
Zatem, przykładowo, żeby odczytać pierwszy przystanek dla linii 1, trzeba wywołać w konsoli:
data["linia"][0]["przystanek"][0]["name"]
żeby zobaczyć nazwę 'Wzgórza
Krzesławickie 01' .
Należy przepisać dane do uproszczonego formatu typu słownik, którego kluczem będzie numer linii
tramwajowej (zapisany jako int), a wartością krotka zawierająca wszystkie nazwy przystanków danej linii.
Uwaga: technicznie przystanki oprócz nazw mają też numery, proszę uprościć dane, zapisując wyłącznie nazwy
przystanków bez końcowych numerów (01, 02…).

Proszę wynik konwersji zapisać do pliku wyjściowego (również w formacie .json), np. w ten sposób:
```py
with open('tramwaje_out.json', 'w', encoding='utf-8') as file:
json.dump(trams, file, ensure_ascii=False)
```
W przykładzie założono, że słownik jest pod nazwą trams. Ponadto, proszę wypisać na ekranie następujące
informacje: numer linii – liczba przystanków, posortowane po liczbie przystanków w kolejności malejącej. Na
koniec wypisać również liczbę wszystkich przystanków obsługiwanych przez tramwaje.
