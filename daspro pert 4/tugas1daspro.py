# Sesi input Data karyawan
nama = input("Masukkan nama karyawan: ")
golongan = int(input("Masukkan golongan jabatan (1/2/3): "))
pendidikan = input("Masukkan pendidikan (SMA/D1/D3/S1): ")
jam_kerja = int(input("Masukkan jumlah jam kerja: "))

# SESI GOLONGAN GAJI
if golongan == 1:
    gapok = 3000000
    tj = 0.05 * gapok
elif golongan == 2:
    gapok = 4000000
    tj = 0.10 * gapok
elif golongan == 3:
    gapok = 5000000
    tj = 0.15 * gapok
else:
    print("Golongan tidak valid!")
    gapok = 0
    tj = 0
    
# SESI PENDIDIKAN
if pendidikan.upper() == "SMA":
    tp = 0.025 * gapok
elif pendidikan.upper() == "D1":
    tp = 0.05 * gapok
elif pendidikan.upper() == "D3":
    tp = 0.20 * gapok
elif pendidikan.upper() == "S1":
    tp = 0.30 * gapok
else:
    print("Pendidikan tidak valid!")
    tp = 0
    
# UANG LEMBUR
if jam_kerja > 8:
    honor_lembur = (jam_kerja - 8) * 3500
else:
    honor_lembur = 0
    
# RUMUS TOTAL GAJI
total_gaji = gapok + tj + tp + honor_lembur

# OUTPUT
print("\n--- Rincian Gaji Karyawan ---")
print(f"Nama Karyawan: {nama}")
print(f"Gaji Pokok (Gapok): Rp {gapok:,.2f}")
print(f"Tunjangan Jabatan (TJ): Rp {tj:,.2f}")
print(f"Tunjangan Pendidikan (TP): Rp {tp:,.2f}")
print(f"Honor Lembur: Rp {honor_lembur:,.2f}")
print(f"Total Gaji: Rp {total_gaji:,.2f}")



