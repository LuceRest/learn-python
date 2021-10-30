# Fungsi dengan menggunakan argument sederhana

def siswa(nama):
    print('siswa ini bernama:', nama)

siswa('mario')


print(' ')
print(80 * '-')
print(' ')


# Fungsi dengan menggunakan keywords arguments


def guru(nama,pelajaran):
    print('guru ini bernama:', nama)
    print('mengajar:', pelajaran)

guru(nama='Popong', pelajaran='seni rupa')
print(' ')

guru(pelajaran='olahraga', nama='endang')
print(' ')

guru('olahraga', 'raihan')      # Contoh yang salah, karena akan terjadi salah input


print(' ')
print(80 * '-')
print(' ')


# Fungsi dengan menggunakan default arguments

def penjagaSekolah(nama, shift='siang', galak='tidak'):
    print('penjaga sekolah ini bernama', nama)
    print('shiftnya adalah', shift)
    print('galak?', galak)

penjagaSekolah('Entis')
print(' ')

penjagaSekolah('Maman', shift='malam')
print(' ')

penjagaSekolah('Asep', galak='sangat')
print(' ')

# penjagaSekolah(shift='malam', galak='iya')  # Menghasilkan eror




print(' ')
