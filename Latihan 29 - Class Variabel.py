# Class

class mahasiswa():

    jurusan = "ekonomi"
    jumlah_mahasiswa = 0
    
    def __init__(self, input_nama, input_nim):
        self.nama = input_nama
        self.nim = input_nim

        mahasiswa.jumlah_mahasiswa += 1 

# NB : Apabila ada self-nya, maka itu miliknya instance.
# NB : Apabila tidak ada self-nya, maka itu miliknya class.


# Main Program

print()

otong = mahasiswa("Otong Surotong", 5200411512)
ucup = mahasiswa("Michael Ucup", 5200411513)
cassandra = mahasiswa("cassandra aja", 5200411514)

otong.kegemaran = 'menari'

print(otong.kegemaran)
print(ucup.jurusan)

print('Jumlah mahasiswa :', mahasiswa.jumlah_mahasiswa)


print(" ")
print(80*"-")
print(" ")


print(mahasiswa.__dict__)
print()
print(otong.__dict__)

# NB : <suatu data>.__dict__ -> Berfungsi untuk mengambil semua komponen variabel yang dipunya data tersebut













print()
