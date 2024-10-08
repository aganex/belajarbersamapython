print("Latihan Python Sederhana")

a = input("Masukkan Nama Anda: ")
b = input("Masukkan NIM Anda: ")
c = input("Masukkan Kelas Anda: ")

na = int(input("Masukkan Nilai awal: "))
nb = int(input("Masukkan Nilai akhir: "))

masukan_perintah = input("Masukkan Perintah (+, -, /): ")

if masukan_perintah == '+':
    hasil = na + nb
    operasi = "+"
elif masukan_perintah == '-':
    hasil = na - nb
    operasi = "-"
elif masukan_perintah == '/':
    if nb != 0:
        hasil = na / nb
        operasi = "/"
    else:
        hasil = "Error! Pembagian dengan nol."
        operasi = ""
else:
    hasil = "Pilihan operasi tidak valid!"
    operasi = ""

if operasi:
    print(f"Hasil : {hasil}")
else:
    print(hasil)
