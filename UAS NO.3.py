def hitung_gaji(tarif_per_jam, jam_kerja_per_hari, hari_kerja):
    # Jam kerja normal: 8 jam per hari
    jam_normal = 8
    
    # Hitung total gaji
    total_gaji = 0
    
    for hari in range(hari_kerja):
        if jam_kerja_per_hari <= jam_normal:
            # Jika jam kerja <= 8 jam, gaji normal
            gaji_hari = jam_kerja_per_hari * tarif_per_jam
        else:
            # Jika lebih dari 8 jam, lembur dihitung 1.5x tarif
            jam_lembur = jam_kerja_per_hari - jam_normal
            gaji_hari = (jam_normal * tarif_per_jam) + (jam_lembur * tarif_per_jam * 1.5)
        
        total_gaji += gaji_hari
    
    return total_gaji

# Input data
tarif_per_jam = float(input("Masukkan tarif gaji per jam: Rp "))
jam_kerja_per_hari = float(input("Masukkan jam kerja per hari: "))
hari_kerja = int(input("Masukkan jumlah hari kerja dalam sebulan: "))

# Hitung dan cetak total gaji bulanan
total_gaji_bulanan = hitung_gaji(tarif_per_jam, jam_kerja_per_hari, hari_kerja)
print(f"\nTotal gaji bulanan: Rp {total_gaji_bulanan:,.2f}")