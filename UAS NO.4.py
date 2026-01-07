def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Pembagian dengan nol!"

# Input dua angka
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))

# Pilih operasi
print("\nPilih operasi:")
print("1. Penjumlahan (+)")
print("2. Pengurangan (-)")
print("3. Perkalian (*)")
print("4. Pembagian (/)")

pilihan = input("Masukkan pilihan (1/2/3/4): ")

# Panggil fungsi sesuai pilihan
if pilihan == '1':
    hasil = tambah(angka1, angka2)
    print(f"\nHasil: {angka1} + {angka2} = {hasil}")
elif pilihan == '2':
    hasil = kurang(angka1, angka2)
    print(f"\nHasil: {angka1} - {angka2} = {hasil}")
elif pilihan == '3':
    hasil = kali(angka1, angka2)
    print(f"\nHasil: {angka1} × {angka2} = {hasil}")
elif pilihan == '4':
    hasil = bagi(angka1, angka2)
    print(f"\nHasil: {angka1} ÷ {angka2} = {hasil}")
else:
    print("Pilihan tidak valid!")