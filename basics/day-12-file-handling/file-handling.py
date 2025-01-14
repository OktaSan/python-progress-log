"""
Hari ke-12: Penanganan File di Python
Script ini menunjukkan berbagai metode untuk menangani file di Python,
termasuk operasi membaca (read, readline, readlines) dan menulis (write).
"""

# 1. Menggunakan `read()` untuk membaca seluruh isi file
# Contoh: Membaca semua isi file "contoh.txt"
file_path = r'day-12-file-handling\contoh.txt'

# Membaca isi file
with open(file_path, 'r') as file:
    content = file.read()
    print("Isi file menggunakan read():")
    print(content)

# 2. Menggunakan `readline()` untuk membaca satu baris dalam satu waktu
# Contoh: Membaca baris pertama dari file "contoh.txt"
with open(file_path, 'r') as file:
    first_line = file.readline()
    print("\nBaris pertama dari file menggunakan readline():")
    print(first_line)

# 3. Menggunakan `readlines()` untuk membaca semua baris dan menyimpannya dalam bentuk list
# Contoh: Membaca baris kedua dari file "contoh.txt" menggunakan list
with open(file_path, 'r') as file:
    all_lines = file.readlines()
    if len(all_lines) > 1:
        print("\nBaris kedua dari file menggunakan readlines():")
        print(all_lines[1])
    else:
        print("\nFile tidak memiliki baris kedua.")

# 4. Menulis isi ke dalam file menggunakan `write()`
# Catatan: Operasi menulis membutuhkan mode 'w' (write) atau 'a' (append).
write_file_path = r'day-12-file-handling\surat.txt'
with open(write_file_path, 'w') as surat:
    surat.write("Hai\nIuwegfai")
    print(f"\nIsi telah ditulis ke dalam file {write_file_path}.")

# 5. Menulis dan membaca isi file menggunakan 'write()' dan 'read()' pada file yang sudah ada.
# Catatan: Digunakan pada file yang sudah ada menggunakan mode 'r+'.
with open(write_file_path, 'r+') as surat:
    surat.write('Hai\nKakak')
    read = surat.read()
    print(f"\nIsi telah ditulis ke dalam file {write_file_path}\nIsi dari .txt file {read}.")

# 6. Menulis isi ke dalam file menggunakan `write()`
# Catatan: Operasi menulis tambahan (bukan menimpa file) membutuhkan moden 'a' (append).
with open(write_file_path, 'a') as surat:
    surat.write("aku\nastronot")
    print(f"\nIsi telah ditulis ke dalam file {write_file_path}.")

# Catatan:
# - Selalu gunakan `with` saat menangani file, karena ini memastikan file ditutup dengan benar setelah operasi selesai.
# - Gunakan `readlines()` saat bekerja dengan banyak baris untuk memprosesnya dalam bentuk list.
# - `write()` akan menimpa file jika file sudah ada; gunakan mode 'a' untuk menambahkan isi ke file.
