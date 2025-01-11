# n = 1

# print('PERKALIAN 1 HINGGA 10 \n')
# for i in range(n, 11):
#     for n in range(1, 11):
#         result = i * n
#         print(f'{i} x {n} = {result}')
#     print('=' * 20)


# #matriks
A = [[1, 2],
    [3, 4]]
B = [[4, 3],
    [2, 1]]

hasil = [[0, 0],
        [0, 0]]


#matrik multiplication
for i in range(len(A)):
    for j in range(len(B)):
        for k in range(len(B[0])):
            hasil[i][j] += A[i][k] * B[k][j]

print(hasil)

# # for baris in range(len(A)):
# #     for kolom in range(len(A[0])):
# #         hasil[baris][kolom] = A[baris][kolom] - B[baris][kolom]
# #         print(hasil[baris][kolom], end=' ')
# #     print('')
# #unpacking
# data = (1, 2, 3, 4, 5)
# a, b, *c = data
# print(a, b, c)

#list
# data = [[1,2], [3,4],[5,6]]

# for a, b in data:
#     print(a, b)

kamus = {'nama' : 'okta', 'umur' : 13}

#.item() => hanya untuk dictionary
for key, value in kamus.items():
    print(f'{key} : {value}')



dataMhs = ['okta', 'hahah']

for index, value in enumerate(dataMhs):
    print(index, value)