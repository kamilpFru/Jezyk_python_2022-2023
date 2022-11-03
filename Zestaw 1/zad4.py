x = int(input("Enter x: "))
y = int(input("Enter y: "))

for i in range(x + 1):
    for j in range(y):
        if j == y - 1:
            print('+---+', end='')
        else:
            print("+---", end='')
    print('')
    
    if i == x: break
    for k in range(y):
        if k == y - 1:
            print('|   |', end='')
        else:
            print('|   ', end='')
    print('')
        