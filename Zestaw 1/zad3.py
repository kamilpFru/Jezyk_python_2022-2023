val = input("Enter value: ")

print('|', end='')
for i in range(int(val) - 1):
    print ('....|', end='')
print('')
for i in range(int(val)):
    if i < 9:
        print (i, '   ', end='')
    else:
        print (i, '  ', end='')
    

