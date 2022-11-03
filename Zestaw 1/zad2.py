arr1 = input("Enter numbers: ")   
lista = list(map(int,arr1.split(' ')))

def factor(x):
    values = []
    y = 2
    while (x != 1):
        if x % y == 0:
            values.append(y)
            x /= y
        else:
            y += 1
    values.sort()
    return values

def printPower(x):
    l1 = factor(x)
    my_dict = {i:l1.count(i) for i in l1}

    for i, j in my_dict.items():
        if j > 1:
            print(i, '^', j, end='', sep='')
        else:
            print(i, end='')
        if i != list(my_dict)[-1]:
            print('*', end='')
    print('')

for i in lista:
    printPower(i)