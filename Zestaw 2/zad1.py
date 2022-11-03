list1 = [3, 4, [2, [1, 2, [7, 8], 3, 4], 3, 4], 5, 6, 7]

def addNumber(lista, number):
    for i in range(len(lista)):
        if isinstance(lista[i], list):
            addNumber(lista[i], number)
            break
        if i == len(lista) - 1 and not isinstance(lista[i], list):
            lista.append(number)

addNumber(list1, 9)
print(list1)