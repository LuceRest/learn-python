# Teknik Looping
print()


nama_band = ['Payung Teduh',
            'Fourtwnty',
            'Dialog Dini Hari',
            'Mr. Sonjaya',
            'Parahyena']

kumpulan_lagu = ['Akad',
        'Zona Nyaman',
        'Rumahku',
        'Sang Filsuf',
        'Sindoro']



# Looping Biasa

iterasi = 0

for band1 in nama_band:
    print('no:', iterasi, ' nama band', band1)
    iterasi += 1


print(' ')
print(80 * '-')
print(' ')


# Looping dengan menggunakan enumerate

for index, band2 in enumerate(nama_band):                            # enumerate akan mereturn indeks dan band2
                                                                     # enumerate berfungsi untuk mengurutkan.
    print(index, ':', band2)


print(' ')
print(80 * '-')
print(' ')


# Looping dengan menggunakan zip

for band3, lagu1 in zip(nama_band, kumpulan_lagu):                  # zip berfungsi untuk menggabungkan list.
    print(band3, 'menyanyikan lagu yang berjudul :', lagu1)

# NB : Apabila ingin menggunakan zip, maka ukuran list harus sama (Harus berpasangan).


print(' ')
print(80 * '-')
print(' ')


# Looping dengan menggunakan set

playlist = {'baby baby', 'ada apa dengan cinta', 'cenat-cenut', 'jaran goyang'}

for lagu2 in sorted(playlist):                                      # sorted(<variabel>) berfungsi untuk mengurutkan data pada suatu variabel.
    print(lagu2)


print(' ')
print(80 * '-')
print(' ')


# Looping dengan menggunakan dictionary

playlist2 = {'Payung Teduh' : 'Akad',
            'Fourtwnty' : 'Zona Nyaman',
            'Dialog Dini Hari' : 'Rumahku',
            }

for a in playlist2.keys():                                          # <variabel>.keys() berfungsi untuk memakai key-nya saja.
    print(a)

print(' ')


for b in playlist2.values():                                        # <variabel>.values() berfungsi untuk memakai value-nya saja.
    print(b)

print(' ')

for c in playlist2.items():                                         # <variabel>.items() berfungsi untuk memakai key dan value.
    print(c)


print(' ')
print(80 * '-')
print(' ')


# Looping dengan menggunakan reversed dan range

for d in reversed(range(1,10,1)):
    print(d)

# reversed() -> Berfungsi untuk membalikan data.
# range(<start>, <stop>, <step/jarak>) -> Berfungsi untuk menampilkan urutan bilangan.

    



print()
