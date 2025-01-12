# def bola(r):
#     volume = ((4/3) * 3.14 * r**3)
#     luasLing = 3.14 * r**2
#     return volume, luasLing

# #menggunakan unpacking
# volBola, luasLing = bola(5)
# print(f'volume bola : {volBola}')
# print(f'volume lingkaran : {luasLing}')

print('kalkulator bangun datar dan bangun ruas')
print('pilih kategori:')
print('1. bangun datar')
print('2.bangun ruang')

bangunDatar = ['1. persegi', '2. persegi panjang', '3. segitiga', '4. jajar genjang', '5. lingkaran', '6. trapesium', '7. belah ketupat', '8. layang-layang']
bangunRuang = ['1. kubus', '2. balok']

user = int(input('silahkan pilih kategoi: '))

def bangunDatarUser(user):
    if user == 1:
        print('\n LIST BANGUN DATAR')
        print(bangunDatar[0])
        print(bangunDatar[1])
        print(bangunDatar[2])
        print(bangunDatar[3])
        print(bangunDatar[4])
        print(bangunDatar[5])
        print(bangunDatar[6])
        print(bangunDatar[7])

        userOpsi = int(input('silahkan pilih bangun datar:'))
        if userOpsi == 1:
            sisi = float(input('masukkan sisi: '))
            print(f'hasil dari luas persegi: {sisi * sisi}')
        elif userOpsi == 2:
            panjang = float(input('masukkan panjang:'))
            lebar = float(input('masukkan lebar: '))
            print(f'luas persegi panjang: {panjang * lebar}')
        elif userOpsi == 3:
            alas = float(input('masukkan alas: '))
            tinggi = float(input('masukkan tinggi: '))
            setengah = 1/2
            print(f'hasil dari luas segitiga yaitu: {setengah * alas * tinggi}')
        elif userOpsi == 4:
            alas = float(input('masukkan alas: '))
            tinggi = float(input('masukkan tinggi: '))
            print(f'luas dari jajar genjang: {alas * tinggi}')
        elif userOpsi == 5:
            Pi = 3.14
            ruas = float(input('masukkan ruas: '))
            print(f'hasil dari luas lingkaran: {Pi * (ruas**2)}')
        elif userOpsi == 6:
            setengah = 1/2
            sisiAtas = float(input('sisi atas: '))
            sisiBawah = float('sisi bawah: ')
            tinggi = float('tinggi: ')
            print(f'luas dari trapesium: {setengah * (sisiAtas * sisiBawah) * tinggi}')
        elif userOpsi == 7:
            setengah = 1/2
            diagonal1 = float(input('masukkan diagonal 1: '))
            diagonal2 = float(input('masukkan diagonal 2: '))
            print(f'luas belah ketupat: {setengah * diagonal1 * diagonal2}')
        else:
            setengah = 1/2
            diagonal1 = float(input('masukkan diagonal 1: '))
            diagonal2 = float(input('masukkan diagonal 2: '))
            print(f'luas belah ketupat: {setengah * diagonal1 * diagonal2}')
    elif user == 2:
        print('\n LIST BANGUN RUANG')
        print(bangunRuang[0])
        print(bangunRuang[1])

        userOpsi = float(input('pilih opsi bangun ruang: '))
        if userOpsi == 1:
            sisi = float(input('masukkan sisi: '))
            print(f'volume dari kubus: {sisi**3}')
        else:
            panjang = float(input('masukkan panjang: '))
            lebar = float(input('masukka lebar: '))
            tinggi = float(input('masukkan tinggi: '))
            print(f'volume balok: {panjang * lebar * tinggi}')
    else:
        print('SILAHKAN PULANG!!!!')

    return 

bangunDatarUser(1)