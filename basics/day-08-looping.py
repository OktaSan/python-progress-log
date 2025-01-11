#looping
#for

num = list(range(1, 101))

#len() => untuk cek berapa isi element
#print(len(num)) # 16 element

# for n in num:
#     print()

#range(start, stop, step)
# for i in range(0, 99, 2):
#     print(i)

# # untuk mengakses element secara mundur
# for i in range(0, 99, 2):
#     print(i)











#hitung faktorial
n = 5
hasil = 1
for i in reversed(range(1, n + 1)):
    hasil *= i
    print(f'nilai i = {i}')
    print(f'hasil sekarang = {hasil}')