def tentukan_kategori(usia):
    if 0 <= usia <= 5:
        return "Balita"
    elif 6 <= usia <= 12:
        return "Anak-anak"
    elif 13 <= usia <= 17:
        return "Remaja"
    elif 18 <= usia <= 59:
        return "Dewasa"
    elif usia >= 60:
        return "Lansia"
    else:
        return "Usia tidak valid"

# Input usia dari pengguna
usia = int(input("Masukkan usia: "))

# Tentukan kategori menggunakan if-elif-else
kategori = tentukan_kategori(usia)

# Cetak hasil kategori
print(f"Kategori usia {usia} tahun adalah: {kategori}")