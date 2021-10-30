# List sebagai iterable
gorengan = ['bakwan','cireng','tahu','tempe goreng','ubi goreng']

for g in gorengan:
    print(g)
    print(len(g))


print(" ")
print(80*"-")
print(" ")


# String sebagai iterable

bakwan = 'bakwan'

for i in bakwan:
    print(i)


print(" ")
print(80*"-")
print(" ")


# For di dalam for
buah = ['semangka', 'jeruk', 'apel','anggur']
sayur = ['kangkung', 'wortel', 'tomat', 'kentang']

Daftar_belanja = [gorengan,buah,sayur]

for subDataBelanja in Daftar_belanja:
    print(subDataBelanja)
    for komponen in subDataBelanja:
        print(komponen)




print(" ")
print(" ")

