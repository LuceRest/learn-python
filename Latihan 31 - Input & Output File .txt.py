# Input & Output File

# Mode-mode dalam membuka file text

"""
w   = write mode            -> Menulis dan menghapus file lama, jika file tidak ada maka akan dibuat file baru.
r   = read mode only        -> Hanya bisa baca.
a   = appending mode        -> Menambahkan data di akhir baris.
r+  = write and read mode   -> Bisa menulis dan membaca.

"""


# Membuat file text

file = open("Latihan 31 - Input & Output File - Data.txt.txt",'w')

file.write('ini adalah data text yang dibuat dengan menggunakan python')
file.write('\nini baris kedua')
file.write('\nini baris ketiga')
file.write('\nini baris keempat')


file.close()


# Membaca file text

file2 = open("Latihan 31 - Input & Output File - Data.txt.txt", 'r')

# print(file2.read(50))
print(file2.readline())
print(file2.readline())

file2.close()


# Appending mode

file3 = open("Latihan 31 - Input & Output File - Data.txt.txt", 'a')

file3.write("\nbaris ini dibuat dengan menggunakan mode append")

file3.close()


# NB : <variabel file text> = open("<lokasi file text>", "<mode>")
# NB : print(<variabel file text>.read(<batas jumlah karakter>)) -> Berfungsi untuk menampilkan isi file text dengan batas karakter yang ditentukan.
# NB : print(<variabel file text>.readline(<batas jumlah karakter>)) -> Berfungsi untuk menampilkan isi file text pada suatu baris dengan batas karakter yang ditentukan.

