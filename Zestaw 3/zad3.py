import math

def odwracanie1(L, left, right):

    if right < left:
        left, right = right, left

    x = math.floor((right - left) / 2)
    i = 0
    while(i <= x):
        L[left], L[right] = L[right], L[left]
        right += 1
        left -= 1
        i += 1
    print(L)

def odwracanie2(L, left, right):
    L[left], L[right] = L[right], L[left]

    if left < right:
        odwracanie2(L, left + 1, right - 1)
    else:
        print(L)

lista = [3, 4, 5, 6, 7, 8, 9, 10]
left, right = 2, 5

print(lista)
odwracanie1(lista, left, right)
odwracanie2(lista, left, right)