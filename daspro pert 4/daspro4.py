kd_baju = input("Masukan kode Baju [SP/AD] : ")
ukuran = input("Masukan Ukuran Baju [S/M] : ")

if kd_baju == "SP" or kd_baju == "sp":
  merk = "SuperDry"
  if ukuran == "S" or ukuran == "s":
    harga = 450000
  elif ukuran == "M" or ukuran == "m":
    harga = 500000
  else:
    harga = "Ukuran tidak tersedia"
    
elif kd_baju == "AD" or kd_baju == "ad":
  merk = "Adidas"
  if ukuran == "S" or ukuran == "s":
    harga = 650000
  elif ukuran == "M" or ukuran == "m":
    harga = 700000
  else:
    harga = 0

else:
  merk = "Anda salah input kode merk"
  harga = 0

print("-------------------------")
print("Merk Baju : " + str(merk))
print("Harga Baju : Rp.", harga)