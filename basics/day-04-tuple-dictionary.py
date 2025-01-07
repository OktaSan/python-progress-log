#membuat tuple (tuple bersifat immutable/tetap)
nama = ("yanti", "yanto", "yentre")
print(nama)

#membuat dictionary (key-value)
kamusBahasaInggris = {
    "nama" : "name",
    "umur" : "age",
    "tidur" : "sleep"
}
print(kamusBahasaInggris)

#menambahkan 1 data ke dakam dictionary
kamusBahasaInggris["meja"] = "table"
print(kamusBahasaInggris["meja"])

#.get() => berfungsi untuk cek nilai yang tidak ada di dalam dictionary
#tanpa menimbulkan error
print(kamusBahasaInggris.get("makan")) # => menghasilkan None jika nilai kosong

#.update() => untuk menambahkan nilai/data ke dalam dictionary dalam jumlah banyak 
kamusBahasaInggris.update({
    "minum" : "drink",
    "bendera" : "flag",
    "tanah" : "dirt"
})
print(kamusBahasaInggris)

#menghapus data di dalam dictionary hampir sama seperti di list

#latihan soal tuple di dalam tuple
dataMhs = {
    "022" : {
        "nama" : "kyra",
        "namaOrtu" : {
            "ibu" : "nana",
            "ayah" : "badang"
        }
    }
}

result1 = dataMhs["022"]["nama"]
result2 = dataMhs["022"]["namaOrtu"]["ibu"]
result3 = dataMhs["022"]["namaOrtu"]["ayah"]
print(f"Mahasiswa bernama {result1} dari ibu {result2} dan bapak {result3}")