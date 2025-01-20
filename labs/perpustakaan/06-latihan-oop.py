class Buku:
    def __init__(self, judul, penulis, tahun_terbit, ISBN):
        self.judul = judul
        self.penulis = penulis
        self.tahun_terbit = tahun_terbit
        self.ISBN = ISBN

    def tampilkan_info(self):
        print(f'Judul buku : {self.judul}\nPenulis : {self.penulis}\nTahun terbit buku : {self.tahun_terbit}\n ISBN : {self.ISBN}')

    def __str__(self):
        return f'{self.judul}, {self.penulis}, {self.tahun_terbit}, {self.ISBN}'

class Buku_fiksi(Buku):
    def __init__(self, judul, penulis, tahun_terbit, ISBN, genre):
        super().__init__(judul, penulis, tahun_terbit, ISBN)
        self.genre = genre
    
    def tampilkan_info(self):
        print(f'Judul buku : {self.judul}')

class BukuNonFiksi(Buku):
    def __init__(self, judul, penulis, tahun_terbit, ISBN, subjek):
        super().__init__(judul, penulis, tahun_terbit, ISBN)
        self.subjek = subjek

    def tampilkan_info(self):
        print(f'Judul buku : {self.judul}')

#class utama Perpustakaan 
class Perpustakaan:
    def __init__(self):
        self.daftar_buku = []

    def tambah_buku(self, buku):
        write_file_path = r'perpustakaan\dbs.txt'
        self.daftar_buku.append(buku)
        with open(write_file_path, 'a') as file:
            for buku in self.daftar_buku:
                file.write(str(buku) + '\n')
            print(f"\nIsi telah ditulis ke dalam file {write_file_path}.")
            

    def hapus_buku(self,ISBN):
        write_file_path = r'perpustakaan\dbs.txt'
        with open(write_file_path, 'r') as file:
            line = file.readlines()
        with open(write_file_path, 'w') as file:
            for l in line:
                if ISBN not in l:
                    file.write(l)
                    print(f'\nBuku dengan ISBN {ISBN} telah berhasil dihapus dari database.')
                else:
                    print(f'Buku dengan ISBN {ISBN} tidak ditemukan dalam database.')
        with open(write_file_path, 'r') as file:
            print(f'\nIsi dari database sekarang adalahh : {file.read()}')
        

    def cari_buku(self, judul):
        write_file_path = r'perpustakaan\dbs.txt'
        with open(write_file_path, 'r') as file:
            for line in file:
                if judul in line:
                    print(f'Buku dengan judul {judul} ditemukan dalam database.')
                    print(f'Informasi buku : {line}')
                    break
            else:
                print(f'Buku dengan judul {judul} tidak ditemukan dalam database.')     

    def tampilkan_semua_buku(self):
        if self.daftar_buku:
            for buku in self.daftar_buku:
                buku.tampilkan_info()

# Membuat objek buku dan perpustakaan
buku1 = BukuNonFiksi('hfaiewh', 'Makoto Shinkai', 201, '2794723221011', 'Romantis')
perpustakaan = Perpustakaan()

# Menambah buku ke perpustakaan
# Perpustakaan.tambah_buku(perpustakaan, buku1)
Perpustakaan.cari_buku(perpustakaan, 'hfaiewh')