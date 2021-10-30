# Membuat GUI Sederhana
import tkinter
from tkinter import Label

main_window = tkinter.Tk()

def event_tekan():
    label2 = tkinter.Label(main_window, text="Unchhh, aku ditekan ^_^")
    label2.pack()

label = tkinter.Label(main_window, text="Halo, saya adalah \n GUI sederhana dengan \n menggunakan python")
label.pack()

tombol = tkinter.Button(main_window, text="Tekan Akuh", command = event_tekan)
tombol.pack()

main_window.mainloop()


# NB : <variabel>.mainloop  -> Berfungsi untuk membuat program menunggu hingga diclose apabila telah selesai.
# NB : <variabel>.pack      -> Berfungsi untuk menaruh suatu teks di dalamnya.
# NB : <variabel>.Button    -> Berfungsi untuk membuat suatu tombol.
# NB : <variabel>.Button(<lokasi>, text = "<isi teks>", command = <perintah saat ditekan>)