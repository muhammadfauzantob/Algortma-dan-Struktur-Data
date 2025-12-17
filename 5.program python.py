nama_list = []

while True:
    print("\nMenu:")
    print("1. Tambah nama")
    print("2. Hapus nama")
    print("3. Tampilkan semua nama")
    print("4. Keluar")

    pilihan = input("Pilih menu (1-4): ")

    if pilihan == "1":
        nama = input("Masukkan nama: ")
        nama_list.append(nama)
        print("Nama berhasil ditambahkan.")

    elif pilihan == "2":
        nama = input("Masukkan nama yang ingin dihapus: ")
        if nama in nama_list:
            nama_list.remove(nama)
            print("Nama berhasil dihapus.")
        else:
            print("Nama tidak ditemukan.")

    elif pilihan == "3":
        print("\nDaftar Nama:")
        for n in nama_list:
            print("-", n)

    elif pilihan == "4":
        print("Keluar dari program.")
        break

    else:
        print("Pilihan tidak valid.")