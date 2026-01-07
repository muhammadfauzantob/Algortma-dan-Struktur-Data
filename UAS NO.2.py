# Fungsi untuk mencetak pola bintang
def cetak_pola_bintang(jumlah_baris):
    for i in range(1, jumlah_baris + 1):
        print('*' * i)

# Input jumlah baris
jumlah_baris = int(input("Masukkan jumlah baris: "))

# Cetak pola sesuai jumlah baris
cetak_pola_bintang(jumlah_baris)