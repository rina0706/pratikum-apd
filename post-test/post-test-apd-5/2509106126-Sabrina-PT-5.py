dataPotion_Minecraft = {
    1: {"nama": "Potion of Strength", "durasi": "3:00", "efek": "Meningkatkan damage"},
    2: {"nama": "Healing Potion", "durasi": "Instant", "efek": "Memulihkan kesehatan"},
    3: {"nama": "Potion of Swiftness", "durasi": "3:00", "efek": "Meningkatkan kecepatan"}
}

print("=== DATA POTION MINECRAFT ===")
i = 1
while i <= len(dataPotion_Minecraft):
    print(f"{i}. {dataPotion_Minecraft[i]['nama']} | Durasi: {dataPotion_Minecraft[i]['durasi']} | Efek: {dataPotion_Minecraft[i]['efek']}")
    i = i + 1

print("\n=== PROGRAM CRUD DASAR DENGAN DICTIONARY ===")

menu = "0"
while menu != "5":
    print("\nPilih menu:")
    print("1. Tambah Data Potion")
    print("2. Lihat Data Potion")
    print("3. Ubah Data Potion")
    print("4. Hapus Data Potion")
    print("5. Keluar")
    
    menu = input("Masukkan pilihan (1-5): ")
    
    if menu == "1":
        # Tambah data potion baru
        print("\n=== TAMBAH DATA POTION ===")
        nama = input("Masukkan nama potion: ")
        durasi = input("Masukkan durasi potion (contoh: 3:00, Instant): ")
        efek = input("Masukkan efek potion: ")
        
        # Cari ID terakhir
        if dataPotion_Minecraft:
            id_terakhir = max(dataPotion_Minecraft.keys())
            id_baru = id_terakhir + 1
        else:
            id_baru = 1
            
        dataPotion_Minecraft[id_baru] = {
            "nama": nama,
            "durasi": durasi,
            "efek": efek
        }
        print(f"Data potion '{nama}' berhasil ditambahkan dengan ID {id_baru}!")
        
    elif menu == "2":
        # Lihat semua data potion
        print("\n=== DAFTAR DATA POTION ===")
        if len(dataPotion_Minecraft) == 0:
            print("Tidak ada data potion")
        else:
            i = 1
            while i <= len(dataPotion_Minecraft):
                if i in dataPotion_Minecraft:
                    print(f"ID: {i}")
                    print(f"  Nama   : {dataPotion_Minecraft[i]['nama']}")
                    print(f"  Durasi : {dataPotion_Minecraft[i]['durasi']}")
                    print(f"  Efek   : {dataPotion_Minecraft[i]['efek']}")
                    print("-" * 40)
                i = i + 1
                
    elif menu == "3":
        # Ubah data potion
        print("\n=== UBAH DATA POTION ===")
        if len(dataPotion_Minecraft) == 0:
            print("Tidak ada data untuk diubah")
        else:
            # Tampilkan daftar ID yang tersedia
            print("ID yang tersedia:", list(dataPotion_Minecraft.keys()))
            
            id_potion = input("Masukkan ID potion yang akan diubah: ")
            if id_potion.isdigit():
                id_int = int(id_potion)
                if id_int in dataPotion_Minecraft:
                    print(f"\nData saat ini:")
                    print(f"Nama   : {dataPotion_Minecraft[id_int]['nama']}")
                    print(f"Durasi : {dataPotion_Minecraft[id_int]['durasi']}")
                    print(f"Efek   : {dataPotion_Minecraft[id_int]['efek']}")
                    
                    print("\nMasukkan data baru (kosongkan jika tidak ingin mengubah):")
                    nama_baru = input("Nama baru: ") or dataPotion_Minecraft[id_int]['nama']
                    durasi_baru = input("Durasi baru: ") or dataPotion_Minecraft[id_int]['durasi']
                    efek_baru = input("Efek baru: ") or dataPotion_Minecraft[id_int]['efek']
                    
                    dataPotion_Minecraft[id_int] = {
                        "nama": nama_baru,
                        "durasi": durasi_baru,
                        "efek": efek_baru
                    }
                    print("Data potion berhasil diubah!")
                else:
                    print("ID tidak ditemukan!")
            else:
                print("Input harus angka!")
            
    elif menu == "4":
        # Hapus data potion
        print("\n=== HAPUS DATA POTION ===")
        if len(dataPotion_Minecraft) == 0:
            print("Tidak ada data untuk dihapus")
        else:
            print("ID yang tersedia:", list(dataPotion_Minecraft.keys()))
            
            id_potion = input("Masukkan ID potion yang akan dihapus: ")
            if id_potion.isdigit():
                id_int = int(id_potion)
                if id_int in dataPotion_Minecraft:
                    nama_potion = dataPotion_Minecraft[id_int]['nama']
                    del dataPotion_Minecraft[id_int]
                    print(f"Data potion '{nama_potion}' berhasil dihapus!")
                else:
                    print("ID tidak ditemukan!")
            else:
                print("Input harus angka!")
                
    elif menu == "5":
        # Keluar dan tampilkan data akhir
        print("\n=== DATA AKHIR POTION MINECRAFT ===")
        if len(dataPotion_Minecraft) == 0:
            print("Tidak ada data potion")
        else:
            # Urutkan ID sebelum menampilkan
            sorted_ids = sorted(dataPotion_Minecraft.keys())
            for id_potion in sorted_ids:
                print(f"ID: {id_potion}")
                print(f"  Nama   : {dataPotion_Minecraft[id_potion]['nama']}")
                print(f"  Durasi : {dataPotion_Minecraft[id_potion]['durasi']}")
                print(f"  Efek   : {dataPotion_Minecraft[id_potion]['efek']}")
                print("-" * 40)
        print("Program selesai. Terima kasih!")
        
    else:
        print("Pilihan tidak valid! Silakan pilih 1-5.")