# if statements
nilai = 50

if nilai == 75: # equal eksplisit
    print("nilai anda:", nilai)


if nilai is 60: # equal
    print("nilai anda:", nilai)

if nilai is not 60: # not equal
    print("nilai anda:", nilai)


print(80*"-")

# elif statement
nilai = 10
if 80 <= nilai <= 100:
    print("nilai anda adalah A")
elif 70 <= nilai < 80:
    print("nilai anda adalah B")
elif 60 <= nilai < 70:
    print("nilai anda adalah C")
elif 50 <= nilai < 60:
    print("nilai anda adalah D, segera lakukan perbaikan")
else:
    print("""
    nilai anda adalah E
    maaf anda tidak lulus mata kuliah ini
    Goblok sih akwoakowkokawk
    """)
    

print(80*"-")


# Operator logika untuk list dan string
print("Operator logika untuk list dan string")
print(" ")

gorengan = ["bakwan","cireng","bala-bala","gehu","pisang goreng","pukis","risoles"]
beli = "cireng"

if beli in gorengan:
    print('Mamang bilang, "ya saya jual',beli,'"')

if not beli in gorengan:
    print('"Saya gak jual',beli,'"')

karakter = "z"
if karakter in beli:
    print("ada",karakter,"di",beli)
else:
    print("tidak ada",karakter,"di",beli)




print(" ")
print(" ")




