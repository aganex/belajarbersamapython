jumlah_data = int(input("Masukkan jumlah data: "))

data_mahasiswa = []

for i in range(1, jumlah_data + 1):
    print(f"\nData ke-{i}")
    nim = input("Masukkan NIM Anda: ")
    nilai_uts = int(input("Masukkan nilai UTS Anda: "))
    nilai_uas = int(input("Masukkan nilai UAS Anda: "))
    total_nilai = nilai_uts + nilai_uas
    data_mahasiswa.append((nim, nilai_uts, nilai_uas, total_nilai))

print("\nTabel Data Mahasiswa")
print("------------------------------------------------")
print("NIM         | UTS | UAS | Total")
print("------------------------------------------------")
for data in data_mahasiswa:
    nim, uts, uas, total = data
    print(f"{nim} | {uts:3} | {uas:3} | {total:5}")
print("------------------------------------------------")
