produk = []


print('Menu Pemesanan Online')
print('1. Manajement Produk')
print('2. Pemesanan')
print('3. Histori Transaksi')

userPilih = int(input('Silahkan pilih menu : '))
while userPilih == 1 or 2 or 3: 
    
    if userPilih == 1:
        print('Menu Manajement Produk')
        print('1. Tambah Produk')
        print('2. Lihat Produk')
        print('3. Hapus Produk')

        userManajement = int(input('Silahkan pilih menu : '))
        if userManajement == 1:
            id = int(input('Buat ID produk : '))
            nama = input('Masukkan nama produk : ')
            harga = float(input('Masukkan harga produk : '))
            stok = int(input('Masukkan stok produk : '))
            produkBaru = {'id' : id, 'nama' : nama, 'harga' : harga, 'stok' : stok}
            produk.append(produkBaru)
            print(f'Produk {nama} berhasil di tambahkan : {produk}')
        elif userManajement == 2:
            print(f'Produk yang tersedia : {produk}')
        else:
            hapus = int(input('Produk ID berapa yang ingin dihapus : '))
            for produksi in produk:
                if produksi['id'] == hapus:
                    produk.remove(produksi)
                    print(f'Produk berhasil di hapus : {produk}')
    elif userPilih == 2:
        with open(r'histori.txt', 'r+') as file:
            nama = input('Masukkan nama : ')
            nomer = int(input('Masukkan nomer telepon : '))
            produkId = int(input('Masukkan ID produk : '))
            jumlahBeli = int(input('Masukkan total produk yang akan dibeli : '))
            #validasi jumlah beli dengan stock
            
    elif userPilih == 3:
        pass
    else:
        pass
    
    print('Menu Pemesanan Online')
    print('1. Manajement Produk')
    print('2. Pemesanan')
    print('3. Histori Transaksi')
    print('4. Keluar dari program')

    userPilih = int(input('Silahkan pilih menu : '))

    while userPilih > 4:
        print('Masukkan menu yang valid !')
        userPilih = int(input('Silahkan pilih menu : '))
    if userPilih == 4:
        print('Anda telah keluar dari program')
        break
    #Tambah produk baru ke daftar produk. Setiap produk memiliki ID, nama, harga, dan stok.