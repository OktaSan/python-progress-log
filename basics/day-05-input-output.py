#menggunakan input() dengan tipe data berbeda-beda (default str)
#str input()
nama = input('masukkan nama anda: ') #bisa juga ditambahkan str

#integer input()
umur = int(input('masukkan umur anda: '))

#float input()
beratBadan = float(input('masukkan berat badan anda: '))

#boolean input()
benarSalah = bool(input('True or False: ')) #kosongi jika ingin mendapatkan nilai false

#formatted string => memformat output agar lebih mudah di baca semua orang 
print(f'perkenal namaku {nama}, umurku {umur} tahun, dan juga berat badanku {beratBadan}. itu semua adalah fakta {benarSalah}')

#menggunakan operator +
print('perkenalkan namaku, ', nama, 'umurku ', umur, 'tahun, dan juga berat badanku ', beratBadan, '. itu semua adalah fakta ', benarSalah)

#raw string => untuk mencetak nilai mentah tanpa memproses isinya
penjumlahan = input(r'tuliskan penjumlahan beserta jawabannya: ')
print(penjumlahan)

#dua method input yang sering digunakan:
#.lower() => mengubah inputan yang dimasukkan user menjadi huruf kecil semua
warna = input('masukkan warna baju anda: ').lower()
print(warna)

#.upper() => mengubah inputan yang dimasukkan oleh user menjadi huruf besar semua 
mobil = input('masukkan nama mobil: ').upper()
print(mobil)