Barang = ['kunci', 'ember', 'jaket', 'ban', 'mobil']
print(Barang)


print(' ')
print(80 * '-')
print(' ')


# Beberapa method yang bisa digunakan untuk memanipulasi list

# Method untuk menambah data ke dalam list
Barang.append('sepeda')                 # .append() berfungsi untuk menambah data ke dalam list yang ditaruh di belakang
print(Barang)

Barang.extend('donmpet')                # .extend() berfungsi untuk menambah data ke dalam list yang ditaruh di belakang dan dimasukkan per karakter
print(Barang)

Barang.insert(3, 'sepeda')              # .insert() berfungsi untuk menambah data ke dalam list yang dapat ditaruh di manapun. 
                                        # <variabel>.insert(<posisi data baru>, '<data yg ditambahkan>')
print(Barang)

print(' ')
print(80 * '-')
print(' ')

# Method untuk menghitung anggota
print(Barang)
jumlahSepeda = Barang.count('sepeda')   # .count() berfungsi untuk menghitung suatu anggota list
print('Jumlah sepeda adalah: ', jumlahSepeda)

print(' ')
print(80 * '-')
print(' ')

# Method untuk remove data
print(Barang)
Barang.remove('sepeda')                 # .remove() berfungsi untuk meremove suatu anggota list
print(Barang)
# NB : .remove hanya meremove data yang ditemukan pertama kali

print(' ')
print(80 * '-')
print(' ')

# Method untuk reverse list atau membalik list
print(Barang)
Barang.reverse()                        # .reverse() berfungsi untuk mereverse list atau membalik list
print(Barang)

print(' ')
print(80 * '-')
print(' ')

# Method untuk copy isi list suatu variabel ke variabel lainnya
Stuff = Barang.copy()                   # .copy() berfungsi untuk mengcopy isi list suatu variabel lainnya
Stuff.append('gelas')
print(Stuff)
print(Barang)














print(' ')
