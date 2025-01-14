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

with open(r'day-12-file-handling\day-12-praktik\game.txt', 'w') as file:
    filesIsi = file.write(f'{nama}\n{str(jumlahPercobaan)}')

tanya = input('mau baca isi file (y/n) ? ')

if tanya == 'y':
    with open(r'day-12-file-handling\day-12-praktik\game.txt', 'r+') as files:
        fileBaca = files.readlines()
        print(fileBaca[0])
        print(fileBaca[1])