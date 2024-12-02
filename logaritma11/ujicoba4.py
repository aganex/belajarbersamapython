def selection_sort(nilai):
    for pos_tujuan in range(len(nilai)-1,0,-1):
        pos_max=0
        for x in range(1,pos_tujuan+1):
            max_sementara = nilai[pos_max]
            if max_sementara < nilai[x]:
                pos_max= x
        nilai [pos_max], nilai[pos_tujuan]=nilai [pos_tujuan], nilai [pos_max]

nilai = [34,21,1,32,12,31,19, 17,54,39,36,27]

print('Sebelum Sort =', nilai)

selection_sort(nilai)

print('Setelah Sort =', nilai)