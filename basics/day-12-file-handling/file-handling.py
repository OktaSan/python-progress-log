# #read() => untuk membaca isi file
# file = open(r'day-12-file-handling\contoh.txt', 'r')
# baca = file.read()
# print(baca)
# file.close()

# #readline()
# file = open(r'day-12-file-handling\contoh.txt', 'r')
# baca = file.readline()
# print(baca)
# file.close()

# # readlines() => akan disimpan dalam bentuk list
# file = open(r'day-12-file-handling\contoh.txt', 'r')
# baca = file.readlines()
# print(baca[1])
# file.close()

# #.write() harus juga menggunakan mode 'w'

#with

# #note:
# #untuk readline dan readlines bisa menggunakan 2 variabel berbebda

# surat = open(r'day-12-file-handling\surat.txt', 'w')
# isi = surat.write('hai\n iuwegfai')
# surat.close()

angka_asli = 10
nama = input('masukkan nama : ')
angka = int(input('masukkan angka : '))
jumlahPercobaan = 0

while True:
    if angka > angka_asli:
        print('angka kebesaran')
        angka = int(input('masukkan angka : '))
    elif angka < angka_asli:
        print('angka kekecilan')
        angka = int(input('masukkan angka : '))
    else:
        print('benar')
        break
    jumlahPercobaan += 1

print(jumlahPercobaan)

with open(r'day-12-file-handling\game.txt', 'w') as file:
    filesIsi = file.write(f'{nama}\n{str(jumlahPercobaan)}')

tanya = input('mau baca isi file (y/n) ? ')

if tanya == 'y':
    with open(r'day-12-file-handling\game.txt', 'r+') as files:
        fileBaca = files.readlines()
        print(fileBaca[0])
        print(fileBaca[1])