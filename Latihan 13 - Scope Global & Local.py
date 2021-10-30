# Scope variabel : local

namaKucing = 'casandra'
print('nama kucing saya sebelumnya adalah', namaKucing)

def rubahNamaKucing1(namaBaru):
    namaKucing = namaBaru       # Variabel local
    print('saya rubah nama kucing menjadi', namaKucing)

rubahNamaKucing1('katie')
print('nama kucing saya menjadi', namaKucing)   # Tidak berubah karena namaKucing masih scope local


print(' ')
print(80 * '-')
print(' ')


# Scope variabel : global

namaKucing = 'casandra'
print('nama kucing saya sebelumnya adalah', namaKucing)

def rubahNamaKucing2(namaBaru):
    global namaKucing
    namaKucing = namaBaru       # variabel global
    print('saya rubah nama kucing menjadi', namaKucing)

rubahNamaKucing2('katie')
print('nama kucing saya menjadi', namaKucing)


print(' ')
print(80 * '-')
print(' ')


makananKucing = 'royal canin'
print('kucing saya', namaKucing, 'sedang makan', makananKucing)

def kasiihMakananKucing(makanan, nama):
    global  namaKucing, makananKucing
    namaKucing = nama           # variabel global
    makananKucing = makanan     # variabel global

kasiihMakananKucing('universal', 'alex')

print('nama kucing saya menjadi', namaKucing, 'dan lagi makan', makananKucing)





print(' ')
