harga_ayam = {
    'D': ('Dada', 2500),
    'P': ('Paha', 2000),
    'S': ('Sayap', 1500)
}

print("GEROBAK FRIED CHICKEN")
print("----------------------")
print("Kode   Jenis Potong   Harga")
print("----------------------")
for kode, (jenis, harga) in harga_ayam.items():
    print(f"{kode}      {jenis}         Rp. {harga}")
print("----------------------")

banyak_jenis = int(input("Banyak Jenis: "))
total_pembayaran = 0

for i in range(1, banyak_jenis + 1):
    print(f"\nJenis Ke-{i}")
    kode_potong = input("Kode Potong [D/P/S]: ").upper()
    
    if kode_potong not in harga_ayam:
        print("Kode potong tidak valid.")
        continue
    
    jenis_potong, harga_per_potong = harga_ayam[kode_potong]
    banyak_potong = int(input("Banyak Potong: "))
    
    subtotal = harga_per_potong * banyak_potong
    total_pembayaran += subtotal
    
    print(f"{jenis_potong} - {banyak_potong} potong x Rp. {harga_per_potong} = Rp. {subtotal}")

pajak = total_pembayaran * 0.10
total_dengan_pajak = total_pembayaran + pajak

print("\n----------------------")
print(f"Total Pembayaran Sebelum Pajak: Rp. {total_pembayaran}")
print(f"Pajak 10%                    : Rp. {pajak}")
print(f"Total Pembayaran Setelah Pajak: Rp. {total_dengan_pajak}")
