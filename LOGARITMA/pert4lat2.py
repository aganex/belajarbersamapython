gp = float(input("Masukkan gaji pokok: "))
tj = 0.20 * gp
jk = int(input("Masukkan jam kerja: "))

if jk > 200:
    lembur = (jk - 200) * 20000
else:
    lembur = 0

total_awal = gp + tj + lembur
pajak = 0.10 * total_awal
total_akhir = total_awal - pajak

print("---OUTPUT---")
print(f"Gaji Pokok: {gp}")
print(f"Tunjangan: {tj}")
print(f"Jam Kerja: {jk}")
print(f"Lembur: {lembur}")
print(f"Total Gaji Sebelum Pajak: {total_awal}")
print(f"Pajak: {pajak}")
print(f"Total Gaji Bersih: {total_akhir}")