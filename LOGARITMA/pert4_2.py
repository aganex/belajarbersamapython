Merk = input('Merk Baju P/A/S: ')

if Merk == 'P':
  print('Merk Polo')
  ukuran = input('Ukuran L/M/S: ')
  if ukuran == 'L':
    print('Harga = 300000')
  elif ukuran == 'M':
    print('Harga = 225000')
  else:
    print('Harga = 175000')

elif Merk == 'A':
  print('Merk Alisan')
  ukuran = input('Ukuran L/M/S: ')
  if ukuran == 'L':
    print('Harga = 275000')  # Ganti dengan harga Alisan ukuran L
  elif ukuran == 'M':
    print('Harga = 200000')  # Ganti dengan harga Alisan ukuran M
  else:
    print('Harga = 150000')  # Ganti dengan harga Alisan ukuran S

elif Merk == 'S':
  print('Merk StYess')
  ukuran = input('Ukuran L/M/S: ')
  if ukuran == 'L':
    print('Harga = 250000')  # Ganti dengan harga StYess ukuran L
  elif ukuran == 'M':
    print('Harga = 175000')  # Ganti dengan harga StYess ukuran M
  else:
    print('Harga = 125000')  # Ganti dengan harga StYess ukuran S

else:
  print('Merk tidak valid. Silakan masukkan P, A, atau S.')