# Study Case: Aplikasi Manajemen Data user
# Deskripsi:
# Kamu akan membuat aplikasi berbasis terminal sederhana untuk mengelola data user. 

# Aplikasi ini memungkinkan pengguna untuk:
# Menambahkan data user (input & handling error).
# Melihat semua data user (looping).
# Mencari data berdasarkan NIM (conditional).
# Mengupdate data user (dictionary manipulation).
# Menghapus data user (list/dictionary).

# Fitur Utama:
# Tipe Data dan Variabel: Gunakan list, tuple, dan dictionary untuk menyimpan data.
# Input & Output: Ambil data dari pengguna dan tampilkan data dengan rapi.
# Conditional: Cek apakah password yang diinput valid.
# Looping dan Nested Looping: Iterasi data untuk pencarian dan tampilan.
# Function: Pisahkan fitur utama dalam fungsi untuk modularitas.
# Error Handling: Tangani input yang salah, seperti password yang duplikat atau data kosong.


dataUsr = []
prodiMhs = ('informatika', 'sistem informasi', 'manajemen rekayasa', 'desain komunikasi visual', 'ekonomi syariah', 'teknik kimia', 'teknik logistik', 'akuntansi', 'manajement', 'teknik industri pertanian')

while True:
    #fungsi menambahkan user baru 
    def tambahUsr():
        print('MASUKKAN BIODATA MAHASISWA')

        i = 0

        #validasi user
        while True:
            username = input('masukkan username : ')
            if username not in dataUsr:
                print('data username berhasil ditambahkan !')
                break
            else:
                print('username sudah terdaftar, gunakan username lain !')

        #validasi password (hanya angka)
        while True:
            try:
                pwd = int(input('masukkan pwd : '))
                print(f'passwrod berhasil ditambahkan !')
                break
            except Exception as e:
                print(f'terjadi error : {e}')

        #validasi prodi 
        while True:
            print('list prodi:')
            for i in range(len(prodiMhs)):
                print(f'{i}. {prodiMhs[i]}')
            prodi = input('masukkan nama prodi : ').lower()
            if prodi in prodiMhs:
                print('prodi berhasil di tambahkan !')
                break
            else:
                print('prodi tidak di temukan, silahkan pilih yang lain !')
            

        dataUsr.append({
            'name' : username,
            'password' : pwd,
            "prodi" : prodi
        })

        for i in range(len(dataUsr)):
            print(f'akun {dataUsr[i]} berhasil buat')


    #fungsi untuk melihat semua user
    def lihatUsr():
        print(dataUsr)

        
    #fungsi untuk mencari user
    def cariUsr():
        cari = input('masukkan nama : ')

        if cari in dataUsr[cari]:
            print(f'username "{cari}" telah ditemukan : {dataUsr[cari]}')
        else:
            print(f'username {cari} tidak ditemukan !')
            cari = input('masukkan nama : ')
                
    
            










    print('MENU')
    print('1. tambahkan user baru')
    print('2. melihat semua user')
    print('3. mencari  user')
    print('4. edit user')
    print('5. hapus user')

    while True:
        try:
            userMenu = int(input('masukkan angka menu : '))
            break
        except Exception as e:
            print(f'terjadi error : {e}')

    match userMenu:
        case 1:
            tambahUsr()
        case 2:
            lihatUsr()
        case 3:
            cariUsr()

    tanya = input('kembali ke menu/keluar dari program (y/n) : ')

    if tanya == 'y' :
        True
    else:
        False











#CODE BELUM SELESAIIIIII