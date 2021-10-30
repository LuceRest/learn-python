Data = [1,4,9,16,25,36,49,64]

# Mengakses list
Subdata1 = Data[3]
Subdata2 = Data[-3]


# Memotong list
Subdata3 = Data[2:4]
Subdata4 = Data[4:]
Subdata5 = Data[:-4]
# NB : <variabel>[<awal>:<akhir>]

Data2 = [100,200,300,400,500,600,700,800]


# Menambah list
Data3 = Data + Data2


# Menambah content dari list
#print(Data) # Sebelum ditambah

#Data[4] = 87 
#print(Data) # Sesudah ditambah
# Hapus " # " di depan syntax untuk melihat perubahannya


# Mengcopy list ke variabel baru
#a = Data[:]
#a[7] = 87

#print(Data)
#print(a)
# Hapus " # " di depan syntax untuk melihat perubahannya


# Merubah content list dengan menggunakan metode slicing
#Data[3:5] = [11,12]

#print(Data)
# Hapus " # " di depan syntax untuk melihat perubahannya


# List dalam list

x = [Data, Data2]

#print(x)
# Hapus " # " di depan syntax untuk melihat perubahannya


# Mengakses list dalam multidimensional list

y = x[0][2]
z = x[1][4]

# print(x)
# print(y)
# print(z)
# Hapus " # " di depan syntax untuk melihat perubahannya


# Metode untuk list

#print(Data) # Sebelum ditambah

Data.append(20)
Data.append(Data2)

# print(Data) # Sesudah ditambah
# Hapus " # " di depan syntax untuk melihat perubahannya



# Function yang bisa digunakan kepada list

panjang_list = len(Data)
# NB : " len() berfungsi untuk menghitung jumlah content yang ada di dalam list"

print(Data)
print(panjang_list)


