#Penjumlahan
a = 1 + 5
print('1 + 5 =',a)
#Pengurangan
a = 6 - 2
print('6 - 2 =',a)
#Perkalian
a = 3 * 5
print('3 * 5 =',a)
#Pembagian
a = 15 / 3
print('15 / 3 =',a)
#Modulus
a = 15 % 2
print('15 % 2 =',a)
#Pangkat
a = 8 ** 2
print('8 ** 2 =',a)
#Pembagian bulat
a = 17 // 3
print('17 // 3 =',a)


#sama dengan =
c = 1 == 1
print('Apakah 1 == 1', c)

# Source Program
# a = false, b = false
a = False
b = False
c = a and b
print ("%r and %r = %r" % (a,b,c))
# a = false, b = true
a = False
b = True
c = a and b
print ("%r and %r = %r" % (a,b,c))
# a = true, b = false
a = True
b = False
c = a and b
print ("%r and %r = %r" % (a,b,c))
# a = false, b = false
a = True
b = True
c = a and b
print ("%r and %r = %r" % (a,b,c))

#Penggabungan dua string
kata1 = "Belajar Bahasa Pemrograman Python "
kata2 = "Sangat Menyenangkan"
c = len(kata1)
print(kata1, kata2)
print(kata2, kata2)
#kata pertama dan kedua digabungkan
gabung = kata1 + " " + kata2
print("hasil")
print(gabung)
print(c)

#fungsi index
kata = 'Aisah Zahra'
#dimana posisi karakater Z
print (kata.index('Z'))