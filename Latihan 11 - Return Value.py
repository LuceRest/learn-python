# Fungsi dengan return value
def kuadrat(argumen):
    total = argumen**2
    print('nilai kuadrat dari', argumen, 'adalah', total)
    return total


a = kuadrat(5)
print(a)


print(' ')
print(80 * '-')
print(' ')


# Fungsi dengan return value dan multiple argumen
def tambah(argumen1, argumen2):
    total  = argumen1 + argumen2
    print(argumen1, '+', argumen2, '=', total)
    return total

def kali(argumen1, argumen2):
    total  = argumen1 * argumen2
    print(argumen1, 'x', argumen2, '=', total)
    return total

# b = tambah(3, 4)
c = kali(3, tambah(3,4))
print(c)








print(' ')
