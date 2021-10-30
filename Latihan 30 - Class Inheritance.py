class Ojek():
    
    def __init__(self, nama, transmisi, daerah):
        self.nama = nama
        self.transmisi = transmisi
        self.daerah = daerah

    def cek_id_abang(self):
        print('nama :', self.nama, '\nmotor', self.transmisi, '\ndaerah :', self.daerah)


class Gojek(Ojek):                          # class Gojek mendapatkan warisan (Isi-isinya) dari class Ojek.
    
    def cek_id_abang(self):
        print('cek aplikasi gojek')         # def cek_id_abang() dioverwrite



ojek1 = Ojek('Mario','manual', 'bandung selatan')
ojek2 = Gojek('Jackson','automatic', 'tasikmalaya')

print()
ojek1.cek_id_abang()

print()
ojek2.cek_id_abang()

# NB : Objek diawali dengan huruf besar.
# NB : DRY -> Don't Repeat Yourself
# NB : Inheritance -> Mendapatkan warisan.
# NB : Gojek(Ojek):  -> Class Gojek mendapatkan warisan (Isi-isinya) dari class Ojek.
# NB : pass -> Berfungsi agar ada isinya sehingga tidak eror.












print()
