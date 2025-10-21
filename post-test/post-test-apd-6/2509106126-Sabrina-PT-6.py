dataPotion_Minecraft = {
    1: "Potion of Strength",
    2: "Healing Potion", 
    3: "Potion of Swiftness"
}

print("=== DATA POTION MINECRAFT ===")
for key in dataPotion_Minecraft:
    print(f"{key}. {dataPotion_Minecraft[key]}")

print("\n=== PROGRAM CRUD DASAR ===")

list = "0"
while list != "5":
    print("\nPilih list:")
    print("1. Tambah Data")
    print("2. Lihat Data")
    print("3. Ubah Data")
    print("4. Hapus Data")
    print("5. Keluar")
    
    list = input("Masukkan pilihan (1-5): ")
    
    if list == "1":
        nama = input("Masukkan nama data baru: ")
        if len(dataPotion_Minecraft) == 0:
            new_key = 1
        else:
            new_key = 1
            for key in dataPotion_Minecraft:
                if key >= new_key:
                    new_key = key + 1
        dataPotion_Minecraft[new_key] = nama
        print("Data berhasil ditambah!")
        
    elif list == "2":
        print("\n=== DAFTAR DATA ===")
        if len(dataPotion_Minecraft) == 0:
            print("Tidak ada data")
        else:
            for key in dataPotion_Minecraft:
                print(f"{key}. {dataPotion_Minecraft[key]}")
                
    elif list == "3":
        print("\n=== UBAH DATA ===")
        if len(dataPotion_Minecraft) == 0:
            print("Tidak ada data untuk diubah")
        else:
            for key in dataPotion_Minecraft:
                print(f"{key}. {dataPotion_Minecraft[key]}")
            
            nomor_potion = input("Pilih nomor data yang akan diubah: ")
            nomor_valid = True
            for char in nomor_potion:
                if char < '0' or char > '9':
                    nomor_valid = False
                    break
            
            if nomor_valid and nomor_potion != "":
                nomor_int = int(nomor_potion)
                if nomor_int in dataPotion_Minecraft:
                    nama_baru = input("Masukkan nama baru: ")
                    dataPotion_Minecraft[nomor_int] = nama_baru
                    print("Data berhasil diubah!")
                else:
                    print("Nomor tidak valid!")
            else:
                print("Input harus angka!")
            
    elif list == "4":
        print("\n=== HAPUS DATA ===")
        if len(dataPotion_Minecraft) == 0:
            print("Tidak ada data untuk dihapus")
        else:
            for key in dataPotion_Minecraft:
                print(f"{key}. {dataPotion_Minecraft[key]}")
            
            nomor_potion = input("Pilih nomor data yang akan dihapus: ")
            valid_number = True
            for char in nomor_potion:
                if char < '0' or char > '9':
                    valid_number = False
                    break
            
            if nomor_valid and nomor_potion != "":
                nomor_int = int(nomor_potion)
                if nomor_int in dataPotion_Minecraft:
                    del dataPotion_Minecraft[nomor_int]
                    print("Data berhasil dihapus!")
                else:
                    print("Nomor tidak valid!")
            else:
                print("Input harus angka!")
            
    elif list == "5":
        print("\n=== DATA AKHIR ===")
        for key in dataPotion_Minecraft:
            print(f"{key}. {dataPotion_Minecraft[key]}")
        print("Program selesai. Terima kasih!")
        
    else:
        print("Pilihan tidak valid! Silakan pilih 1-5.")