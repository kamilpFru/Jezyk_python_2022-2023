def fun(x): 
    number = bin(x).replace('b', '0')  
    list = number.split('1')
    if number[len(number) - 1] != '1':
        list.pop()
    if number[0] != '1':
        list.pop(0)
    print(len(max(list, key=len)))

fun(1041)