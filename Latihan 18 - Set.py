# Set (Himpunan)

superhero = {'wiro sableng', 
            'si buta dari goa hantu', 
            'gundala', 
            'gatot kaca'}

print(superhero)

# NB : Set tidak memperhatikan urutan.
# NB : Set tidak akan memperhatikan jumlah dari suatu data (Hanya apa saja datanya).
# NB : Set tidak dapat diindeks.
# NB : Set digunakan saat hanya membutuhkan jenis data.


superhero.add('mak lampir')             # .add - > Berfungsi untuk menambah data pada set.
superhero.add('gundala') 
print(superhero)

print(sorted(superhero))                # sorted(<variabel>) -> Berfungsi untuk menugurutkan data set (himpunan).


print(' ')
print(80 * '-')
print(' ')


hero = set()

hero.add('wiro sableng')
hero.add('gundala')
hero.add('saras 008')
hero.add(212)

print(hero)


print(' ')
print(80 * '-')
print(' ')


ganjil = {1,3,5,7,9}
genap = {2,4,6,8,10}
prima = {2,3,5,7}

print(ganjil.union(genap))              # <variabel 1>.union(<variabel 2>) -> Berfungsi sebagai union/gabungan pada himpunan.
print(ganjil.intersection(genap))       # <variabel 1>.intersection(<variabel 2>) -> Berfungsi sebagai intersection/irisan pada himpunan. 
print(ganjil.intersection(prima))       # <variabel 1>.intersection(<variabel 2>) -> Berfungsi sebagai intersection/irisan pada himpunan. 





print()
