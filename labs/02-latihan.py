# Study Case 2: Daftar Belanja
# Buatlah program yang memungkinkan pengguna untuk membuat dan mengelola daftar belanja. 
# Pengguna bisa menambahkan item ke dalam daftar, menghapus item, menampilkan daftar, dan mencari item tertentu dalam daftar.

# Tugas:
# Program harus memiliki menu yang memungkinkan pengguna memilih antara menambahkan, menghapus, menampilkan, atau mencari item dalam daftar belanja.
# Gunakan list untuk menyimpan item belanjaan.
# Pastikan input yang diberikan pengguna benar dan valid, misalnya tidak ada item yang duplikat dalam daftar.
# Gunakan conditional statements untuk menentukan aksi yang dilakukan sesuai pilihan pengguna

#buat list kosong sebagai keranjang
daftar = []

#list buah yang tersedia di toko
buah = [
    "apel", "pisang", "jeruk", "anggur", "nanas", "mangga", "semangka", "strawberry", "bluberi", "persik",
    "plum", "pir", "ceri", "lemon", "pepaya", "kelapa", "aprikot", "melon", "alpukat", "kiwi", "leci",
    "jambu", "buah naga", "markisa", "ara", "kurma", "jeruk keprok", "mandalika", "kedondong", "raspberry", "blackberry",
    "gooseberry", "delima", "nangka", "belimbing", "longan", "pomelo", "kesemek", "nektarin", "lime", "clementine",
    "quince", "mulberry", "sirsak", "rambutan", "durian", "acai", "ciku", "elderberry", "hawthorn", "marula",
    "roti buah", "apel pir", "tamarind", "ceri bing", "apel manis", "sirsak", "jujube", "ceri", "karambola", "leci",
    "cranberry", "lingonberry", "bramley", "sea buckthorn", "yunnan hackberry", "tamarillo", "tangan buddha", "kacang yam", "miracle fruit", "tamarind",
    "kismis putih", "salak", "chayote", "cherimoya", "fennel", "pear cactus", "sage fruit", "melon pahit", "chayote", "buah naga",
    "zukini", "nance", "melon galia", "nangka", "mangosteen", "moringa", "buah oregano", "buah jamaika", "mulberry buah", "satsuma",
    "pir berduri", "zaitun", "lada", "sirsak", "pepino", "bilberry", "melon musim dingin", "pawpaw", "loquat", "pineberry",
    "sapote hitam", "jeruk manis", "squash", "jahe", "miracle fruit", "cabai", "jeruk darah", "clementine", "melon pahit", "grapefruit"
]

tanya = input('apakah anda ingin membuat daftar belanja ? (y/n)').lower()
while tanya == 'y':

    print('=============== menu ===============')
    print('1. tambahkan item (wajib untuk yang baru menggunakan)')
    print('2. hapus item')
    print('3. tampilkan item')
    print('4. cek item')
    print('5. keluar dari program')

    #input user untuk memilih menu
    user = input('silahkan pilih menu dengan angka: ')

    #validasi input user
    while user not in ['1', '2', '3', '4', '5']:
        print('masukkan menu yang valid!')
        user = input('silahkan pilih menu dengan angka: ')

    #proses selanjunya pada pemilihan menu
    match user:

        #menambahkan item ke daftar
        case '1':
            print('==========MASUKKAN SATU ITEM DAHULU!!!==========')
            userAdd = input('masukkan item: ')
            #validasi apakah item ada di toko
            if userAdd in buah:
                daftar.append(userAdd)
                print(f'item berhasil di tambahkan: {userAdd}')
            else:
                print(f'buah {userAdd} tidak ada, silahkan cek terlebih dahulu!')

        #hapus item yang ada di daftar
        case '2':
            print('==========HAPUS ITEM==========')
            print('1. hapus item tertentu')
            print('2. hapus semua item')
            print('3. kembali ke menu')

            print(f'item yang ada di daftar belanja: {daftar}')
            userOpsi = input('pilih menu: ').lower()
            
            #hapus item tertentu
            if userOpsi == '1':
                userDel = input('masukkan nama item: ')
                #validasi item yang akan di hapus
                if userDel in daftar:
                    daftar.remove(userDel)
                    print(f'item "{userDel}" berhsil di hapus')
                else:
                    print('item tidak di temukan di dalam daftar')
            #hapus semua item
            elif userOpsi == '2':
                daftar.clear()
                print(f'item yang ada di daftar telah di hapus semua: {daftar}')
            else:
                print('keluar dari menu hapus item.')

        #menampilkan item ke layar
        case '3':
            print('==========TAMPILKAN ITEM==========')
            print(f'daftar item belanja anda: {daftar}')

        #untuk mencari item apakah tersedia di toko atau tidak
        case '4':
            print('==========CARI ITEM==========')
            userCari = input('buah apa yang anda cari di toko ? ').lower()
            if userCari in buah:
                print(f'buah {userCari} tersedia di toko')
            else:
                print(f'tidak ada item {userCari} di daftar belanja anda')


    #untuk looping 
    tanya = input('kembali ke menu (y/n): ').lower()
    
    #finalisasi item
    if tanya == 'n':
        print(f'daftar belanja akhir yang sudah anda tambahkan adalah {daftar}')
    #validasi jawaban
    else:
        while tanya != ('y' or 'n'):
            print('masukkan jawaban yang valid!')
            tanya = input('kembali ke menu (y/n): ').lower()