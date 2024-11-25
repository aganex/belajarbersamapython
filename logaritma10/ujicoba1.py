def mergeSort(X):
    print("Bilangan diurutkan", X)  # Menampilkan data saat proses berlangsung
    if len(X) > 1:  # Jika panjang daftar lebih dari 1, lanjutkan pembagian
        mid = len(X) // 2  # Cari titik tengah untuk membagi array
        lefthalf = X[:mid]  # Bagian kiri
        righthalf = X[mid:]  # Bagian kanan

        # Rekursif ke bagian kiri dan kanan
        mergeSort(lefthalf)
        mergeSort(righthalf)

        # Penggabungan (merge) dengan mengurutkan elemen
        i = j = k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                X[k] = lefthalf[i]
                i += 1
            else:
                X[k] = righthalf[j]
                j += 1
            k += 1

        # Menyalin elemen yang tersisa
        while i < len(lefthalf):
            X[k] = lefthalf[i]
            i += 1
            k += 1
        while j < len(righthalf):
            X[k] = righthalf[j]
            j += 1
            k += 1

        print("Merging", X)  # Menampilkan proses penggabungan

# Data awal
X = [22, 10, 15, 3, 8, 2]
mergeSort(X)  # Memanggil fungsi mergeSort untuk mengurutkan
print("Hasil akhir:", X)  # Menampilkan hasil akhir
