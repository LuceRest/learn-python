# Dictionary (Kamus)

# <variabel> = {<key>:<value>}
# NB : Dictionary diindeks dengan menggunakan key-nya.



print(' ')


member1 = {"ID" : 101,
        "Nama" : "AcilRestu12",
        "Pekerjaan" : "Mahasiswa",
        "Status member" : "Gold"
        }

member2 = {"ID" : 102,
        "Nama" : "EvoryRestu24",
        "Pekerjaan" : "Front End Web Developer",
        "Status member" : "Berlian"
        }

memberList = {101:member1, 102:member2}


print(member1)
print(member1["Nama"])          # <variabel>[<key>] -> Berfungsi untuk memanggil/mengakses value/data pada suatu dictionary.

print(' ') 
print(80 * '-')
print(' ')

print(member1.keys())           # <variabel>.keys() -> Berfungsi untuk memanggil key-nya saja.
print(member1.values())         # <variabel>.values() -> Berfungsi untuk memanggil value-nya saja.
print(member1.items())          # <variabel>.items() -> Berfungsi untuk memanggil key dan value.


print(' ')
print(80 * '-')
print(' ')


print(memberList[101])



print()