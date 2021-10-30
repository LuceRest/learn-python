# Queue (Antrian)

# Modul -> Berfungsi untuk mengimpor dari source code lain

from collections import deque
antrian = deque([1, 2, 3, 4, 5])        # deque() berfungsi untuk menambah dan mengurangi data di depan

print('data sekarang : ', antrian)


print(' ')
print(80 * '-')
print(' ')


# Menambahkan data

antrian.append(6)
print('data masuk : ', 6)
print('data sekarang : ', antrian)

print(' ')

antrian.append(7)
print('data masuk : ', 7)
print('data sekarang : ', antrian)


print(' ')
print(80 * '-')
print(' ')


# Mengurangi antrian

out = antrian.popleft()             # .popleft berfungsi untuk mengurangi/mengelurakan data dari kiri
print('data keluar : ', out)
print('data sekarang : ', antrian)

print(' ')

out = antrian.popleft()             # .popleft berfungsi untuk mengurangi/mengelurakan data dari kiri
print('data keluar : ', out)
print('data sekarang : ', antrian)

print(' ')

out = antrian.popleft()             # .popleft berfungsi untuk mengurangi/mengelurakan data dari kiri
print('data keluar : ', out)
print('data sekarang : ', antrian)
