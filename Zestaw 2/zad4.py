x, y, z, n = [int(i) for i in input("Enter x y z n: ").split()]

lista = [[k, j, i] for k in range(x + 1) for j in range(y + 1) for i in range(z + 1) if i + j + k != n]

# for i in range(x + 1):
#     for j in range(y + 1):
#         for k in range(z + 1):
#             if i + j + k != n:
#                 lista.append([i, j, k])

print(lista)