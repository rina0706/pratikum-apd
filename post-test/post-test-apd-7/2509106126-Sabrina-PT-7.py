dataPotion_Minecraft = {
    1: "Potion of Strength",
    2: "Healing Potion", 
    3: "Potion of Swiftness"
}

program_berjalan = True
jumlah_error = 0

def cari_kode_terbesar():
    """Fungsi tanpa parameter untuk cari kode terbesar"""
    kode_terbesar = 0
    for kode in dataPotion_Minecraft:
        if kode > kode_terbesar:
            kode_terbesar = kode
    return kode_terbesar

def tambah_potion(nama_potion):
    """Fungsi dengan parameter untuk tambah potion"""
    kode_baru = cari_kode_terbesar() + 1
    dataPotion_Minecraft[kode_baru] = nama_potion
    return kode_baru

def hitung_jumlah_data():
    """Fungsi tanpa parameter untuk hitung data"""
    jumlah = 0
    for kode in dataPotion_Minecraft:
        jumlah = jumlah + 1
    return jumlah

def buat_kode_baru():
    """Fungsi tanpa parameter untuk buat kode baru"""
    if hitung_jumlah_data() == 0:
        return 1
    else:
        return cari_kode_terbesar() + 1

def tampilkan_semua_data():
    """Prosedur untuk tampilkan semua data"""
    print("\n=== DAFTAR POTION ===")
    if hitung_jumlah_data() == 0:
        print("Tidak ada data")
    else:
        for kode in dataPotion_Minecraft:
            print(f"{kode}. {dataPotion_Minecraft[kode]}")

def tampilkan_menu():
    """Prosedur untuk tampilkan menu"""
    print("\n" + "="*30)
    print("    PROGRAM POTION MINECRAFT")
    print("="*30)
    print("1. Tambah Data Potion")
    print("2. Lihat Data Potion")
    print("3. Ubah Data Potion")
    print("4. Hapus Data Potion")
    print("5. Keluar")

print("=== DATA AWAL POTION ===")
for kode in dataPotion_Minecraft:
    print(f"{kode}. {dataPotion_Minecraft[kode]}")

while program_berjalan:
    try:
        pilihan_dipilih = False
        percobaan = 0
        
        tampilkan_menu()
        
        while not pilihan_dipilih and percobaan < 2:
            pilihan_input = input("Pilih menu (1-5): ")
            
            adalah_angka = True
            for karakter in pilihan_input:
                if karakter < '0' or karakter > '9':
                    adalah_angka = False
                    break
            
            if adalah_angka and pilihan_input != "":
                pilihan_angka = int(pilihan_input)
                
                if pilihan_angka == 1:
                    pilihan_dipilih = True
                    nama_baru = input("Masukkan nama potion baru: ")
                    
                    if nama_baru == "":
                        print("Error: Nama tidak boleh kosong!")
                        jumlah_error = jumlah_error + 1
                    else:
                        kode_baru = tambah_potion(nama_baru)
                        print(f"Berhasil tambah {nama_baru} dengan kode {kode_baru}")
                        
                elif pilihan_angka == 2:
                    pilihan_dipilih = True
                    tampilkan_semua_data()
                    
                elif pilihan_angka == 3:
                    pilihan_dipilih = True
                    tampilkan_semua_data()
                    
                    if hitung_jumlah_data() > 0:
                        kode_input = input("Pilih kode yang akan diubah: ")
                
                        kode_angka = True
                        for karakter in kode_input:
                            if karakter < '0' or karakter > '9':
                                kode_angka = False
                                break
                        
                        if kode_angka and kode_input != "":
                            kode_int = int(kode_input)
                    
                            kode_ada = False
                            for kode in dataPotion_Minecraft:
                                if kode == kode_int:
                                    kode_ada = True
                                    break
                            
                            if kode_ada:
                                nama_baru = input("Masukkan nama baru: ")
                                if nama_baru == "":
                                    print("Error: Nama tidak boleh kosong!")
                                    jumlah_error = jumlah_error + 1
                                else:
                                    dataPotion_Minecraft[kode_int] = nama_baru
                                    print("Data berhasil diubah!")
                            else:
                                print("Error: Kode tidak ditemukan!")
                                jumlah_error = jumlah_error + 1
                        else:
                            print("Error: Input harus angka!")
                            jumlah_error = jumlah_error + 1
                    
                elif pilihan_angka == 4:
                    pilihan_dipilih = True
                    tampilkan_semua_data()
                    
                    if hitung_jumlah_data() > 0:
                        kode_input = input("Pilih kode yang akan dihapus: ")
                        
                        kode_angka = True
                        for karakter in kode_input:
                            if karakter < '0' or karakter > '9':
                                kode_angka = False
                                break
                        
                        if kode_angka and kode_input != "":
                            kode_int = int(kode_input)
                        
                            kode_ada = False
                            for kode in dataPotion_Minecraft:
                                if kode == kode_int:
                                    kode_ada = True
                                    break
                            
                            if kode_ada:
                                data_baru = {}
                                for kode_lama, nama_lama in dataPotion_Minecraft.items():
                                    if kode_lama != kode_int:
                                        data_baru[kode_lama] = nama_lama
                                
                                dataPotion_Minecraft.clear()
                                
                                for kode_baru, nama_baru in data_baru.items():
                                    dataPotion_Minecraft[kode_baru] = nama_baru
                                
                                print("Data berhasil dihapus!")
                            else:
                                print("Error: Kode tidak ditemukan!")
                                jumlah_error = jumlah_error + 1
                        else:
                            print("Error: Input harus angka!")
                            jumlah_error = jumlah_error + 1
                    
                elif pilihan_angka == 5:
                    pilihan_dipilih = True
                    program_berjalan = False
                    print("\n=== DATA AKHIR ===")
                    tampilkan_semua_data()
                    print("Terima kasih! Program selesai.")
                    
                else:
                    print("Error: Pilih 1-5 saja!")
                    percobaan = percobaan + 1
                    jumlah_error = jumlah_error + 1
            else:
                print("Error: Input harus angka!")
                percobaan = percobaan + 1
                jumlah_error = jumlah_error + 1
        
        if not pilihan_dipilih:
            print("Terlalu banyak percobaan gagal!")
            
    except:
        print("Terjadi error tidak terduga!")
        jumlah_error = jumlah_error + 1

print(f"\nTotal error selama program: {jumlah_error}")