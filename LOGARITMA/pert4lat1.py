print("______________________")
print("--PROGRAM ITUNG GAJI--")
print("Total Gaji anda saat ini 5.000.000")

bp = int(input("Masukkan banyak produk yang terjual: "))
sat = float(input("Masukkan harga satuan produk: "))

total = bp * sat

if bp > 100:
  bonus = 0.20 * total
else:
  bonus = 0.10 * total

gaji_pokok = 5000000
total_gaji = gaji_pokok + bonus

print("=======================")
print("Rincian Gaji Anda:")
print(f"Total Penjualan: Rp {total:,.2f}")
print(f"Bonus: Rp {bonus:,.2f}")
print(f"Gaji Pokok: Rp {gaji_pokok:,.2f}")
print("-----------------------")
print(f"Total Gaji: Rp {total_gaji:,.2f}")