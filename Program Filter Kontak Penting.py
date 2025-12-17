# 1. Meminta input nama kontak (dipisahkan koma)
input_kontak = input("Masukkan nama-nama kontak (pisahkan dengan koma): ")

# 2. Mengubah input menjadi list dan menghapus spasi yang tidak perlu
daftar_kontak = [nama.strip() for nama in input_kontak.split(",")]

print("\n--- Daftar Kontak Penting (≥ 5 Karakter) ---")

jumlah_penting = 0

# 3. Menggunakan 'for' untuk memfilter nama dengan panjang >= 5
for nama in daftar_kontak:
    if len(nama) >= 5:
        print(f"- {nama}")
        jumlah_penting += 1

# 4. Menampilkan jumlah kontak yang memenuhi kriteria
print("-" * 40)
print(f"Jumlah kontak yang terpilih: {jumlah_penting} orang.")