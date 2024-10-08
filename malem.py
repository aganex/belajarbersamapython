

a = input("Nama karyawan :  ")
b = int(input("Masuksan Gaji : "))
c = input("Nama Perusahaan :  ")

formatted_gaji = "{:,}".format(b)

print("Hasil Cetak Adalah")
print("Nama anda    : " +str(a))
print("Gaji             : " + formatted_gaji)
print("Nama Perusahaan    : " +str(c))