# Program Perhitungan Gaji Karyawan

# Fungsi untuk menghitung gaji karyawan
def hitung_gaji(nama, unit_kerja, jam_kerja):
    # Gaji pokok per jam
    gaji_per_jam = 200000
    
    # Total gaji berdasarkan jam kerja
    total_gaji = gaji_per_jam * jam_kerja
    
    # Tunjangan 10% dari total gaji
    tunjangan = 0.10 * total_gaji
    
    # Gaji bersih = total gaji + tunjangan
    gaji_bersih = total_gaji + tunjangan
    
    # Output hasil perhitungan gaji
    print("===== Slip Gaji Karyawan =====")
    print(f"Nama Karyawan : {nama}")
    print(f"Unit Kerja    : {unit_kerja}")
    print(f"Total Gaji    : Rp {total_gaji:,}")
    print(f"Tunjangan     : Rp {tunjangan:,}")
    print(f"Total Gaji Bersih : Rp {gaji_bersih:,}")
    print("=============================")

# Input dari user
nama = input("Masukkan nama karyawan: ")
unit_kerja = input("Masukkan unit kerja karyawan: ")
jam_kerja = int(input("Masukkan jumlah jam kerja: "))

# Panggil fungsi untuk menghitung gaji
hitung_gaji(nama, unit_kerja, jam_kerja)
