#if, elif, else
nilai = 75

if nilai >= 90: #pengecekkan pertama, jika hasilnya true maka akan menampilkan langusung hasil outputnya dan tidak mengerjalan kondis berikutnya.
    print('A+')
elif nilai >= 80: #akan berjalan apabila hasil dari if itu 'false' (anda bisa membuat elif yang banyak).
    print('A-')
else: #kondisi default jika semua pengecekkan itu false maka kondisi 'else' akan berjalan.
    print('tidak lulus!')

#nested if (if bersarang) => di dalam if terdapat if lagi
namaCowok = ['bambang', 'roni', 'gigi']
warnaBaju = ['merah', 'kuning', 'hijau']

cowok = input('masukkan nama cowok: ')
baju = input('masukkan warna baju: ')

if cowok in namaCowok: #fungsi 'in' berguna untuk mengecek apakah data ada di dalam daftar.
    if baju in warnaBaju:
        print(f'cowok yang bernama {cowok} dan berbaju warna {baju} adalah cowok maroon flag')
    else:
        print(f'cowok yang bernama {cowok} dan berbaju warna {baju} adalah cowok red flag')
else:
    print(f'cowok yang bernama {cowok} dan berbaju warna {baju} adalah cowok green flag')

#match-case => pengondisian yang disaranka untuk digunakan ketika ingin melakukan pengecekkan data yang kompleks
x = 4
match x:
    case 1:
        print('x adalah 1')
    case 2:
        print('x adalah 2')
    case 3:
        print('x adalah 3')
    case _:
        print('x tidak cocok dengan manapun!') 
