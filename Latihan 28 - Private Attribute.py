# Class

class mahasiswa():

    jurursan = "Teknik tata boga"
    __nilai = 0                                         # __nilai sebagai private attribute.
    
    def __init__(self, input_nama, input_nim):
        self.nama = input_nama                          # self.nama sebagai public attribute.
        self.nim = input_nim                            # self.nama sebagai public attribute.
        self.__nilai

    def uts(self, input_nilai):
        self.__nilai += input_nilai

    def uas(self, input_nilai):
        self.__nilai += input_nilai

    def check_status(self):
        if self.__nilai <= 50:
            print(self.nama, 'tidak lulus')
        else:
            print(self.nama, 'lulus')

# NB : __<attribute> -> Berfungsi agar attribute tersebut tidak bisa diakses oleh program dari luar.
# NB : input_nilai di def uts() dengan yang di def uas() itu beda.

# Main Program
print()

otong = mahasiswa("Otong Surotong", 5200411512)
ucup = mahasiswa("Michael Ucup", 5200411513)

otong.uts(10)
otong.uas(50)
otong.check_status()

print()

ucup.uts(5)
ucup.uas(25)
ucup.check_status()








print()
