# Zestaw 1

## Zadanie 1

Narysować odwrócony pusty trójkąt z gwiazdek o zadanej długości nieparzystej, np. dla 11 (każdy
kolejny wiersz maleje o dwie gwiazdki) wyglądać ma:

```text
***********
 *       *
  *     *
   *   *
    * *
     *
```


## Zadanie 2

Napisać program, który czyta podane jako zewnętrzne argumenty liczby naturalne, a następnie każdą rozkłada na czynniki pierwsze (co polega na zapisaniu dowolnej liczby naturalnej za pomocą iloczynu liczb pierwszych). Wymagany jest format wyjściowy w postaci `a1^k1*a2^k2*...*a3`, jeśli `ki==1` to opuszczamy wykładnik potęgi.

Przykładowo, jeśli wywołamy:

```console
zadanie2.py 4407 13041599400
```

to powinno się wypisać (proszę tak to sformatować):

```text
4407 = 3*13*113
130

## Zadanie 3

Napisać program rysujący "miarkę" o zadanej długości.

```text
|....|....|....|....|....|....|....|....|....|....|....|....|
0    1    2    3    4    5    6    7    8    9   10   11   12
```

## Zadanie 4

Napisać program rysujący prostokąt zbudowany z małych kratek. Należy zbudować pełny string,
a potem go wypisać.

Przykładowy prostokąt składający się 2x4 pól ma postać:

```text
+---+---+---+---+
|   |   |   |   |
+---+---+---+---+
|   |   |   |   |
+---+---+---+---+
```

## Zadanie 5

Dla dwóch sekwencji znaleźć: (a) listę elementów występujących jednocześnie w obu sekwencjach
(część wspólną, bez powtórzeń), (b) listę wszystkich elementów z obu sekwencji (sumę, bez
powtórzeń).
