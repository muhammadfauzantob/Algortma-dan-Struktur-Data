# 1. Meminta input jumlah hari belajar
jumlah_hari = int(input("Masukkan jumlah hari belajar: "))

data_belajar = []

# 2. Menggunakan perulangan 'for' untuk memasukkan jam belajar
for i in range(jumlah_hari):
    jam = float(input(f"Masukkan jam belajar hari ke-{i+1}: "))
    
    # 3. Menyimpan data dalam list
    data_belajar.append(jam)

print("\n--- Analisis Produktivitas ---")

hari_produktif = 0

# 4. Menentukan status berdasarkan kriteria
for jam in data_belajar:
    if jam >= 3:
        status = "Produktif"
        hari_produktif += 1
    else:
        status = "Kurang produktif"
    
    print(f"Belajar {jam} jam: {status}")

# 5. Menampilkan jumlah hari produktif
print("-" * 30)
print(f"Total hari produktif: {hari_produktif} hari.")