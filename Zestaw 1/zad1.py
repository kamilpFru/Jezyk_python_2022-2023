val = input("Enter value: ")

def triangle(x):
    y = (x - 1) // 2
    for i in range(y + 1):
        for j in range(i):
            print(' ', end='')
        for k in range(x):
            if i == 0 or k == 0 or k == x - 1:
                print('*', end='')
            else:
                print(' ', end='')
        x = x - 2
        print('')
        
triangle(int(val))
