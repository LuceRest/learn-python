import numpy as np
from PIL import Image

# Package Numpy

a = [1,2,3,4]
b = [5,6,7,8]

c = np.array([1,2,3,4])
d = np.array([5,6,7,8])

print(a + b)
print()
print(c + d)        
# NB : Apabila menggunakan numpy, maka akan dijumlahkan sesuai posisi.


print(' ')
print(80 * '-')
print(' ')

 
# Package Pillow

im = Image.open("Logo UTY.png")

print("Format file  : " + im.format)
print("Ukuran file  : " + str(im.size))
print("Mode file    : " + im.mode)

im.show()


