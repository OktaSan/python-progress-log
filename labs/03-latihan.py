print('=====PPN=====')
# mencari PPN 
kopiSebelumPpn = 15225
kopiSetelahPpn = 16900
ppn = 0

#mencari berapa persen PPN
ppn += int((((kopiSetelahPpn - kopiSebelumPpn) / kopiSebelumPpn)) * 100 )

#untuk mendapatkan nilai PPN
ppnTotal = kopiSetelahPpn - kopiSebelumPpn

#untuk menampilkan hasil
print(f'harga sabun muka sebelum ppn : {kopiSebelumPpn}')
print(f'PPN : {ppn}%')
print(f'nilai PPN : {ppnTotal}')
print(f'harga sabun muka setelah PPN : {kopiSetelahPpn}')

print('')

print('=====mencari harga sebelum ppn=====')
#mencari nilai sebelum PPN
stardewValley = 0
stardewValleyPpn = 77700
ppn = 1 + (11/100)

stardewValley = stardewValleyPpn / ppn

print(f'harga awal dari stardewValley : {stardewValley}')

print('')

print('=====mencari harga setelah ppn=====')
#mencari harga setelah ppn
laptop = 7000000
laptopPpn= 0
ppn = 1 + (11/100)

laptopPpn = laptop * ppn
print(f'harga setelah ppn dari laptop : {int(laptopPpn)}')