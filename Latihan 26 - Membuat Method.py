# Class

class mahasiswa():
    nama = 'nama'
    nim = '402'

    def belajar(self, kondisi):                                             # self -> Berfungsi untuk mengidentifikasi suatu class digunakan oleh siapa.
        print(self.nama, 'dengan nim', self.nim, 'saya belajar', kondisi)   # self.<attribute> -> Berfungsi untuk memanggil attribute untuk setiap instance yang memakai class tersebut.

    def tidur(self):                                                        # self -> Berfungsi untuk mengidentifikasi suatu class digunakan oleh siapa.
        print(self.nama, 'tidur di kelas')                                  # self.<attribute> -> Berfungsi untuk memanggil attribute untuk setiap instance yang memakai class tersebut.



# Main Program

otong = mahasiswa()
ucup = mahasiswa()

otong.nama = "Otong Surotong"
ucup.nama = "Michael Ucup"

otong.belajar("dengan giat")
print()
ucup.tidur()


# NB : Method adalah fungsi yang menempel atau berada di dalam kelas.
# NB : Fungsi saja adalah fungsi yang berada di luar kelas.
# NB : Class harus diletakkan di atas.
# NB : self -> Berfungsi untuk mengidentifikasi suatu class digunakan oleh siapa.
# NB : self.<attribute> -> Berfungsi untuk memanggil attribute untuk setiap instance yang memakai class tersebut.





print()
