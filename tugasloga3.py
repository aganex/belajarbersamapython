input_a = float(input("Masukan Angka: "))
a = input_a

while a < 12:
    if a + 4 > 12:
        print(12)
        break
    print(a)
    a += 4
    print(a)