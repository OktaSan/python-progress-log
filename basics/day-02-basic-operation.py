#basic operators (aritmatika, perbandingan, logika)
#aritmatika
print(25*"=","OPERATOR ARITMATIKA",25*"=")
print("'+' : penjumlahan")
print("'-' : pengurangan")
print("'*' : perkalian")
print("'/' : pembagian dengan hasil desimal")
print("'//' : pembagian dengan hasil dibulatkan kebawah")
print("'%' : modulus/sisa bagi")
print("'**' : pengkat")

print()

print(25*"=","Perbandingan",25*"=")
print("'==' : sama dengan")
print("'!=' : tidak sama dengan")
print("'>' : lebih dari")
print("'<' : kurang dari")
print("'>=' : lebih dari/sama dengan")
print("'<=' : kurang dari/sama dengan")

print()

print(25*"=","Logika",25*"=")
print("'and' : kedua nilai harus True agar hasilnya True")
print("'or' : salah satu nilai bernilai True maka hasilnya True")
print("'not' : kebalikkannya")

print()

print(25*"=","Latihan",25*"=")
#latihan soal menghitung luas lingkaran
r = 7
pi = 22/7
hasil = pi * (r**2) 
print('hasil dari luas lingkaran adalah: ', hasil)

print()

#latihan menghitung diskon
hargaSepatu = 120000
diskon = 12/100
hargaPotongan = hargaSepatu * (diskon)
hargaFinalSepatu = hargaSepatu - hargaPotongan
print(f"harga sepatu {hargaSepatu} dan mendapatkan diskon {hargaPotongan}, maka harga yang harus dibayar ialah {hargaFinalSepatu}")