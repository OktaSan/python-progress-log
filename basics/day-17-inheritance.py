import math

#inheritance => pewarisan

#parent class => super class
class Penggguna:
    def __init__(self, nama, id_anggota):
        self.nama = nama
        self.id_anggota = id_anggota

    def info(self):
        print(f'Nama : {self.nama}\nAnggota ID : {self.id_anggota}')

#child class => sub class
class Admin(Penggguna):
    def __init__(self, nama, id_anggota, jabatan):
        super().__init__(nama, id_anggota)
        self.jabatan = jabatan

    def remove_pengguna(self, nama_akun):
        print(f'Akun dengan nama {nama_akun} telah berhasil dihapus')

    def info(self): #method overriding => polymorphism
        super().info()
        print(f'Jabatan : {self.jabatan}')


adm1 = Admin('okta', 'adm001', 'DEV')
adm1.info()

print('='*70)

class Calculator:
    def __init__(self,angka1, angka2):
        self.angka1 = angka1
        self.angka2 = angka2
    
    def penjumlahan(self):
        hasil = self.angka1 + self.angka2
        print(f'hasil dari {self.angka1} + {self.angka2} = {hasil}')

    def pengurangan(self):
        hasil = self.angka1 - self.angka2
        print(f'hasil dari {self.angka1} - {self.angka2} = {hasil}')

    def pembagian(self):
        hasil = self.angka1 / self.angka2
        print(f'hasil dari {self.angka1} / {self.angka2} = {hasil}')

    def perkalian(self):
        hasil = self.angka1 * self.angka2
        print(f'hasil dari {self.angka1} * {self.angka2} = {hasil}')


class Scientific(Calculator):
    def __init__(self, angka1, angka2):
        super().__init__(angka1, angka2)

    def penjumlahan_sin(self):
        hasil = math.sin(math.radians(self.angka1)) + math.sin(math.radians(self.angka2))
        print(f'hasil dari {math.sin(math.radians(self.angka1))} + {math.sin(math.radians(self.angka2))} = {hasil:.2f}')

    def pengurangan_sin(self):
        hasil = math.sin(math.radians(self.angka1)) - math.sin(math.radians(self.angka2))
        print(f'hasil dari {math.sin(math.radians(self.angka1))} - {math.sin(math.radians(self.angka2))} = {hasil:.2f}')

    def pembagian_sin(self):
        hasil = math.sin(math.radians(self.angka1)) / math.sin(math.radians(self.angka2))
        print(f'hasil dari {math.sin(math.radians(self.angka1))} / {math.sin(math.radians(self.angka2))} = {hasil:.2f}')

    def perkalian_sin(self):
        hasil = math.sin(math.radians(self.angka1)) * math.sin(math.radians(self.angka2))
        print(f'hasil dari {math.sin(math.radians(self.angka1))} * {math.sin(math.radians(self.angka2))} = {hasil:.2f}')

user = Scientific(30, 60)
user.perkalian_sin()

