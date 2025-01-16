# import math
# print(math.sqrt(10))

# import math as m
# print(m.sqrt(9))

#import spesifik menjadi fungsi lokal
# from math import sqrt, sin
# print(sqrt(100))

#import semua fungsi ke lokal dan tidak efisien
# from math import *

# import random
# print(random.random()) # dalam rentang 0 sampai 1

# angka = random.randint(1, 1000)
# print(angka)

# nama = ['okta', 'keyra', 'liora']
# print(random.choice(nama))
# print(random.choices(nama, k=4))
# print(random.sample(nama, k=2))

import myModule 

print(myModule.pass_generator())