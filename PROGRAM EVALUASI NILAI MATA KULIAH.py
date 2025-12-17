jumlah_mk = int(input("Masukkan jumlah mata kuliah: "))
nilai = []
tidak_lulus = 0

for i in range(jumlah_mk):
    n = int(input(f"Masukkan nilai mata kuliah ke-{i+1}: "))
    nilai.append(n)

    if n >= 85:
        print("Kategori: Sangat Baik")
    elif 70 <= n <= 84:
        print("Kategori: Baik")
    elif 60 <= n <= 69:
        print("Kategori: Cukup")
    else:
        print("Kategori: Tidak Lulus")
        tidak_lulus += 1

print("Jumlah mata kuliah tidak lulus:", tidak_lulus)
