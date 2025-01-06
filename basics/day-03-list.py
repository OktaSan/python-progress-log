#membuat list[]
buah = ["apel", "mangga", "semangka"]

#memodifikasi isi list
buah[1] = "jeruk"

#menambakan elemnt ke dalam list
#.append() => untuk menambahkan 1 data saja ke dalam list
buah.append("salak")
print(buah)

#.insert() => untuk menambahkan data ke dalam urutan index tertentu di dalam list
buah.insert(1, "nangka")
print(buah)

#menghapus element pada list
#.remove() => bertujuan untuk menghapus element tertentu dalam list
buah.remove("apel")
print(buah)

#.pop() => defaultnya menghapus mulai index paling belakang (-1)
angka = [1, 2, 3]
angka.pop(0)
print(f"baru {angka}")

#.clear() => menghapus habis isi dari list tersebut dan menyisakan list kosong
angka.clear()
print(angka)

#.sort()
angkaAcak = [7, 1, 2, 5, 3]
angkaAcak.sort() # => mengurutkan dari terkecil ke terbesar
print(angkaAcak)
angkaAcak.sort(reverse=True) # => mengurutkan dari terbesar ke terkecil
print(angkaAcak)

#mengakses nilai tertentu di dalam list dengan masukkan indexnya
print(buah[1]) # => output: apel
