def BubbleSort(X):
    for i in range(len(X)-1,0,-1):
        Max=0
        for I in range(1,i+1):
            if X[I]<X[Max]:
                Max = I
        temp = X[i]
        X[i] = X[Max]
        X[Max] = temp

Hasil = [22,10,15,3,8,2]
BubbleSort(Hasil)
print(Hasil)