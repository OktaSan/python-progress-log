# Study Case 1: Kalkulator Sederhana
# Buatlah program yang meminta pengguna untuk memasukkan dua angka, kemudian pilih operasi matematika (penjumlahan, pengurangan, perkalian, pembagian) 
# untuk dilakukan pada kedua angka tersebut. Program ini harus menggunakan variabel, tipe data (angka dan string), operator, dan input/output.

# Tugas:
# Program harus meminta input dua angka dari pengguna.
# Program harus meminta input jenis operasi yang ingin dilakukan (misalnya: +, -, *, /).
# Program harus menampilkan hasil dari operasi yang dipilih.
# pastikan program menangani kemungkinan kesalahan (misalnya pembagian dengan nol).

#untuk tampilan memilih operasi
print('====kalkulator sederhana====')
print('penjumlahan')
print('pengurangan')
print('perkalian')
print('pembagian')

#memasukkan input dari user
pilih = input('pilih salah satu operasi diatas: ').lower()
nilai1 = int(input('masukkan angka pertama: '))
nilai2 = int(input('masukkan angka kedua: '))

#melakukan pengecekkan lalu pengoperasian
match pilih:
    case 'penjumlahan':
        print(f'hasil dari {nilai1} + {nilai2} = {nilai1 + nilai2}')
    case 'pengurangan':
        print(f'hasil dari {nilai1} - {nilai2} = {nilai1 - nilai2}')   
    case 'perkalian':
        print(f'hasil dari {nilai1} x {nilai2} = {nilai1 * nilai2}')
    case 'pembagian':
        if (nilai1 and nilai2) == 0:
            print(f'pemabagian tidak boleh 0')
        else:
            print(f'hasil dari {nilai1} / {nilai2} = {nilai1 / nilai2}')
    case _:
        print('masukkan data yang valid!')