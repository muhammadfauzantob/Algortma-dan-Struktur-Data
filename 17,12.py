# 1. Meminta input jumlah hari
jumlah_hari = int(input("Masukkan jumlah hari pengeluaran: "))

daftar_pengeluaran = []

# 2. Menggunakan loop 'for' untuk memasukkan data
for i in range(jumlah_hari):
    pengeluaran = float(input(f"Masukkan pengeluaran hari ke-{i+1}: "))
    
    # 3. Menyimpan data dalam list
    daftar_pengeluaran.append(pengeluaran)

print("\n--- Ringkasan Pengeluaran ---")

# 4. Menentukan status (Boros/Hemat) untuk setiap hari
for index, biaya in enumerate(daftar_pengeluaran):
    status = "Boros" if biaya >= 100000 else "Hemat"
    print(f"Hari ke-{index+1}: Rp {biaya:,.0f} ({status})")

# 5. Menampilkan total dan rata-rata
total = sum(daftar_pengeluaran)
rata_rata = total / jumlah_hari

print("-" * 30)
print(f"Total Pengeluaran    : Rp {total:,.0f}")
print(f"Rata-rata Per Hari   : Rp {rata_rata:,.0f}")