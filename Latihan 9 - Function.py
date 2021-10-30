# Membuat fungsi

def suaraayam():
    print('kukuruyuk!!!!!')

suaraayam()


print('')
print(80 * '-')
print('')


# Membuat fungsi di dalam fungsi

def hargaayam():
    suaraayam()
    print('harga ayam per 1 kg adalah Rp. 20.000,-')

hargaayam()


print('')
print(80 * '-')
print('')


# Membuat fungsi dengan input argumen

def hargatotalayam(kg):
    suaraayam()
    harga = 20000
    hargaTotal = kg * harga
    print('harga',kg,'kg ayam adalah',hargaTotal)


hargatotalayam(2)





print('')

