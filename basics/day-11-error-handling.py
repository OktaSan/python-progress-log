#try => untuk mencoba code-code yang berpotensi error
try:
    print('code pertama')
    num = int(input('masukkan angka : '))
    hasil = 10/num

#except ExceptionType => jika code error maka akan ditangkap oleh except
except ZeroDivisionError:
    print('ga boleh dibagi nol !')

#else => jika code tidak ada yang error maka else berjalan
else:
    print(f'hasil dari pembagian 10/{num} : {hasil}')

#finally => akan selalu tereksekusi meskipun code error/tidak error
finally:
    print('='*40)


try:
    print('code kedua')
    num2 = int(input('masukkan nilai : '))

#mengunakan Exception akan menringkas semua error handling tanpa kita harus menuliskan jenis errornya satu-satu    
except Exception as e: # => lebih disarankan menggunakan ini ketimbang yang di code pertama
    print(f'terjadi error : {e}')


#KESIMPULAN
# error handling akan kita gunakan ketika ada suatu code yang memiliki potensi error
# dan juga manfaat dari menggunakan error handiling ialah code tetap berjalan walaupun
# terjadi error, namun hanya akan peringatan saja dan code tetap berjalanjut berjalan 