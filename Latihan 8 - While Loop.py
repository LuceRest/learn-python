angka = 0

while angka < 5:
    print('nilai angka adalah:',angka)
    angka = angka + 1


print('di luar while')

print(' ')
print(80*"-")
print(' ')

# Menggunakan variabel boolean
start = True    # Variabel boolean
angka = 0

while start:
    print('di dalam while')
    if angka is 100:
        start = False
        print('oke angka 100 ditemukan')
    angka += 1


print('di luar while')


print(' ')
print(80*"-")
print(' ')


# Else, Break, Continue, Pass pada while

angka = 0

while angka < 10:

    if angka is 5:
        # print('checkpoint1') 
        # break
        angka += 1
        # continue
        # pass
        # print('checkpoint2')
    print('nilai angka adalah:',angka)
    angka += 1
else:
    print('nilai angka di akhir while adalah',angka)

print('di luar while')

# NB : Hati-hati apabila menggunakan continue pada while loop

print(' ')







