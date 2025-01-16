import bahan
import random

print(bahan.title)
print('''Aturan Permainan :
1. Selamatkan 'Budi' dengan cara menjawab 1 pertanyaan dengan benar!
2. Budi hanya memiliki 6 nyawa!
3. 1 Kesalahan akan mengurangi 1 nyawa Budi!
''')

user = input('Apakah anda siap menyelamatkan budi (y/n) ? ')

if user == 'y':
    with open(r'pertanyaan.txt', 'r+') as file1, open(r'jawaban.txt', 'r+') as file2:
            pertanyaan = file1.readlines()
            jawaban = file2.readlines()
            heart = 6
            i = 0
            for i in range(0, 6):
                print(bahan.hangman[i])
                random_num = random.randint(1,100)
                tanya = pertanyaan[random_num]
                jwb = jawaban[random_num].strip().lower()
                print(tanya)
