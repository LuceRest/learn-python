# Class

class mahasiswa():

    def __init__(self, input_nama, input_nim):
        self.nama = input_nama
        self.nim = input_nim

    def belajar(self, kondisi):
        print(self.nama,'saya belajar', kondisi)   

    def tidur(self):           
        print(self.nama, 'tidur di kelas')                                  



# Main Program

otong = mahasiswa("Otong Surotong", 5200411512)
print(otong.nama)
print(otong.nim)

print()

otong.nama = "Atang Suratang"
print(otong.nama)

otong.belajar('dengan giat')

# ucup = mahasiswa()
# ucup.nama = "Michael Ucup"


# NB : __init__( ) -> Berfungsi untuk memanggil langsung attribute tanpa harus dipanggil terlebih dahulu (Langsung jalan sendiri).
# NB : __init__() -> Akan dijalankan saat melakukan inisialisasi objek.

