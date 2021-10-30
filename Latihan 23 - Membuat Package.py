# Cara 1 Membuat Package : Import file-file .py lain dari folder lain

# from Latihan_23_Membuat_Package_Sains import  Latihan_23_Membuat_Package_Fisika, Latihan_23_Membuat_Package_Matematika

# fisika1 = Latihan_23_Membuat_Package_Fisika.kecepatan(3,4)
# print(fisika1)

# matematika1 = Latihan_23_Membuat_Package_Matematika.tambah(4,5)
# print(matematika1)

# NB : from <nama folder lokasi file lain> import <file lain 1>, <file lain 2> -> Berfungsi untuk memanggil file-file lain yang berada di folder lain.
# NB : Folder yang berisi file-file lain yang akan diimport namanya harus tanpa spasi (Jangan ada spasi di antara kita~). 


print(' ')
print(80 * '-')
print(' ')


# Cara 2 Membuat Package : Menggunakan __init__.py

# Cara 2 v1.0
import Latihan_23_Membuat_Package_Sains

matematika2 = Latihan_23_Membuat_Package_Sains.tambah(5,6)
print(matematika2)

print()

# Cara 2 v2.0
from Latihan_23_Membuat_Package_Sains import kecepatan,kurang

fisika2 = kecepatan(5,2)
print(fisika2)

matematika2_2 = kurang(10,4)
print(matematika2_2)

# NB : __init__.py -> Berfungsi sebagai module yang dapat dipanggil dengan hanya menggunakan nama folder yang berisi beberapa modul.
# NB : __init__.py -> Akan menjadikan suatu folder sebagai package/file-file .py lain yang siap diimport.
# NB : .<nama file .py> -> Arti dari " . " adalah folder sekarang.


print(' ')
print(80 * '-')
print(' ')


# Contoh Penggunaan Package

import math

print(math.cos(0))




print() 
