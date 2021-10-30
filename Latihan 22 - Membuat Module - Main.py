# ---------------------------Cara-Cara Import dari File Lain---------------------------

# Cara 1 : import dari file lain
import Latihan_22_Membuat_Module_matematika
Latihan_22_Membuat_Module_matematika.tambah(3,4)

print(' ')
print(80 * '-')
print(' ')



# Cara 2 : import file lain dengan menjadikannya sebagai variabel baru
import Latihan_22_Membuat_Module_matematika as m
m.tambah(1,2)
print()
m.kurang(2,1)

# NB : import <file lain> as <variabel untuk file lain> -> Berfungsi untuk memanggil file lain dan memasukkannya ke dalam variabel.


print(' ')
print(80 * '-')
print(' ')


# Cara 3 : import variabel di file lain secara spesifik
from Latihan_22_Membuat_Module_matematika import tambah,kurang
tambah(4,5)
kurang(5,4)

# NB : from <file lain> import <variabel 1 di file lain>, <variabel 2 di file lain> -> Berfungsi untuk memanggil variabel-variabel di file lain secara spesifik.


print(' ')
print(80 * '-')
print(' ')


# Cara 4 : import semua variabel di file lain
from Latihan_22_Membuat_Module_matematika import *
tambah(5,6)
kurang(6,5)

# NB : from <file lain> import * -> Berfungsi untuk memanggil semua isi dari file lain.


print(' ')
print(80 * '-')
print(' ')


# Cara 5 : import variabel di file lain secara spesifik lalu menjadikannya sebagai variabel baru
from Latihan_22_Membuat_Module_matematika import tambah as t
t(7,8)

# NB : from <file lain> import <variabel di file lain> as <variabel baru untuk variabel di file lain> -> Berfungsi untuk memanggil variabel di file lain dan memasukkannya ke dalam variabel baru.



print()
