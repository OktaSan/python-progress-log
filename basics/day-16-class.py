# class Mobil:
#     #init => constructor
#     def __init__(self, merk, warna, tahun):
#         #self => untuk memanggil diri sendiri
#         self.merk = merk
#         self.warna = warna
#         self.tahun = tahun

#     def mesin_menyala():
#         pass

# mobilKu = Mobil('honda', 'mmaroon', 2005)

# print(mobilKu.merk)

class Mhs:
    def __init__(self, nama, nim, prodi, angkatan, semester):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi 
        self.angkatan = angkatan
        self.semester = semester

    def tambahSemester(self):
        if self.semester < 14:
            print(f'semester berhasil di perbarui menjadi : {self.semester + 1}')
            print('semester berhasil di tambahkan!')
        else:
            print(f'ini adalah semester terakhir anda')

    def tampilkanDataMhs(self):
        print(f'nama : {self.nama}')
        print(f'nim : {self.nim}')
        print(f'prodi : {self.prodi}')
        print(f'angkatan : {self.angkatan}')
        print(f'semester : {self.semester}')

    def keteranganSemester(self):
        if self.semester <= 2:
            print(f'{self.nama} adalah mahasiswa baru')
        elif self.semester <= 4:
            print(f'{self.nama} adalah mahasiswa menengah')
        elif self.semester <= 7:
            print(f'{self.nama} adalah mahasiswa akhir')
        elif self.semester <= 14:
            print(f'{self.nama} adalah SEPUHHHHHHHHHHH')
        else:
            print(f'{self.nama} LANGSUNG DO!')

mahasiswa = Mhs('wawa', 19392642, 'informatika', 2025, 15)
mahasiswa.tambahSemester()
print('='* 60)
mahasiswa.tampilkanDataMhs()
print('='* 60)
mahasiswa.keteranganSemester()

#encapsulations
#public

#protected => _nama (_)
# class Siswa:
#     def __init__(self, nama):
#         self._nama = nama
#         self.nilai = 0


# siswa1 = Siswa('wawa')
# print(siswa1._nama)

#private ==> __nilai (__)
class Siswa:
    def __init__(self, nama, saldo):
        self.nama = nama
        self.__saldo = saldo

    def printSaldo(self):
        print(f'saldo gw : {self.__saldo}')

    def set_saldo(self, nominal):
        self.__saldo = nominal


siswa1 = Siswa('wawa', 10)
print(siswa1.nama)
siswa1.set_saldo(100000)
siswa1.printSaldo()