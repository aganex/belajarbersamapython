print("++++++++++ DATA DIRI MAHASISWA =============")
nim = input("nim :")
nama = input("Nama Lengkap :")
jurusan = input("Jurusan :")
alamat = input("Alamat :")
uts = int(input("Nilai UTS =  "))
uas = int(input("Nilai Uas =  "))
total = (uts+uas)/2

print("")
print("HASIL CEKTAK DIATAS ADALAH")
print("Nama anda    : " +str(nim))
print("Nim anda    : " +str(nama))
print("jurusan anda    : " +str(jurusan))
print("alamat anda    : " +str(alamat))
print("nilai uts anda    : " +str(uts))
print("nilai uas anda    : " +str(uas))
print("Nilai Akhirr : " +str(total))