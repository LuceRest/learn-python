# def pembagian(a,b):
#     return a/b


# penyebut = int(input("Masukkan angka penyebut?\n"))
# pembilang = int(input("Masukkan angka pembilang?\n"))


# print(pembagian(penyebut, pembilang))


print(' ')
print(80 * '-')
print(' ')


# try:
#     a = 1/0
# except:
#     print("Eror pembagi nol")


# print("Akhir dari program")


print(' ')
print(80 * '-')
print(' ')

"""
while True:
    try:
        angka = int(input("Masukkan angka : "))
        break
    except:
        print("Yang Anda masukkan bukan angka")

print("Berhasil, Anda memasukkan angka : ", angka)
"""


print(' ')
print(80 * '-')
print(' ')


"""
print("Ini adalah program pembagian")
print()

while True:
    try:
        penyebut = int(input("Masukkan angka penyebut : "))
        pembilang = int(input("Masukkan angka pembilang : "))
        hasil = penyebut/pembilang
        break
    except ValueError:
        print("Yang Anda masukkan bukan angka\n")
    except ZeroDivisionError:
        print("Angka pembilang yang Anda masukkan adalah nol, pilih yang lain ya gan\n")

print("Berhasil, hasil pembagiannya adalah : ", hasil)
"""


print(' ')
print(80 * '-')
print(' ')


while True:
    try:
        # import panda
        penyebut = int(input("Masukkan angka penyebut : "))
        pembilang = int(input("Masukkan angka pembilang : "))
        hasil = penyebut/pembilang
        break
    except Exception as err:
        print(err)

print("Berhasil, hasil pembagiannya adalah : ", hasil)








# NB : try & except berfungsi untuk mengatasi eror run time

"""
    Type of Exception Erorrs:
    1. IOError              -> Mengenai input/output fileself.
    2. ImportError          -> Mengenai import package
    3. ValueError
    4. ZeroDivisionError
    5. KeyboardInterupted
    6. EOFError
"""
