#Data awal
data = ["Potion of Strength", "Healing Potion", "Potion of Swiftness"]

print("=== DATA AWAL ===")
i = 0
while i < len(data):
    print(f"{i+1}. {data[i]}")
    i = i + 1

print("\n=== PROGRAM CRUD DASAR ===")

menu = "0"
while menu != "5":
    print("\nPilih menu:")
    print("1. Tambah Data")
    print("2. Lihat Data")
    print("3. Ubah Data")
    print("4. Hapus Data")
    print("5. Keluar")
    
    menu = input("Masukkan pilihan (1-5): ")
    
    if menu == "1":
        # Tambah data
        nama = input("Masukkan nama data baru: ")
        data.append(nama)
        print("Data berhasil ditambah!")
        
    elif menu == "2":
        # Lihat data
        print("\n=== DAFTAR DATA ===")
        if len(data) == 0:
            print("Tidak ada data")
        else:
            i = 0
            while i < len(data):
                print(f"{i+1}. {data[i]}")
                i = i + 1
                
    elif menu == "3":
        # Ubah data
        print("\n=== UBAH DATA ===")
        if len(data) == 0:
            print("Tidak ada data untuk diubah")
        else:
            i = 0
            while i < len(data):
                print(f"{i+1}. {data[i]}")
                i = i + 1
            
            nomor = input("Pilih nomor data yang akan diubah: ")
            if nomor.isdigit():
                nomor_int = int(nomor)
                if nomor_int >= 1 and nomor_int <= len(data):
                    nama_baru = input("Masukkan nama baru: ")
                    data[nomor_int-1] = nama_baru
                    print("Data berhasil diubah!")
                else:
                    print("Nomor tidak valid!")
            else:
                print("Input harus angka!")
            
    elif menu == "4":
        # Hapus data
        print("\n=== HAPUS DATA ===")
        if len(data) == 0:
            print("Tidak ada data untuk dihapus")
        else:
            i = 0
            while i < len(data):
                print(f"{i+1}. {data[i]}")
                i = i + 1
            
            nomor = input("Pilih nomor data yang akan dihapus: ")
            if nomor.isdigit():
                nomor_int = int(nomor)
                if nomor_int >= 1 and nomor_int <= len(data):
                    data.pop(nomor_int-1)
                    print("Data berhasil dihapus!")
                else:
                    print("Nomor tidak valid!")
            else:
                print("Input harus angka!")
            
    elif menu == "5":
        # Keluar
        print("\n=== DATA AKHIR ===")
        i = 0
        while i < len(data):
            print(f"{i+1}. {data[i]}")
            i = i + 1
        print("Program selesai. Terima kasih!")
        
    else:
        print("Pilihan tidak valid! Silakan pilih 1-5.")