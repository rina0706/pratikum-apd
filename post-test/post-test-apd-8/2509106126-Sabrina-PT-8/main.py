from fungsi_tambah import tambah_potion
from fungsi_lihat import tampilkan_semua_data
from fungsi_ubah import ubah_potion
from fungsi_hapus import hapus_potion
from utilitas import hitung_jumlah_data
from data import dataPotion_Minecraft

program_berjalan = True
jumlah_error = 0

def tampilkan_menu():
    print("\n" + "="*30)
    print("  PROGRAM POTION MINECRAFT")
    print("="*30)
    print("1. Tambah Data Potion")
    print("2. Lihat Data Potion")
    print("3. Ubah Data Potion")
    print("4. Hapus Data Potion")
    print("5. Keluar")

print("=== DATA AWAL ===")
tampilkan_semua_data()

while program_berjalan:
    try:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            nama = input("Masukkan nama potion baru: ")
            if nama == "":
                print("Error: Nama tidak boleh kosong!")
                jumlah_error += 1
            else:
                tambah_potion(nama)

        elif pilihan == "2":
            tampilkan_semua_data()

        elif pilihan == "3":
            tampilkan_semua_data()
            if hitung_jumlah_data() > 0:
                kode = int(input("Masukkan kode yang akan diubah: "))
                nama_baru = input("Masukkan nama baru: ")
                ubah_potion(kode, nama_baru)

        elif pilihan == "4":
            tampilkan_semua_data()
            if hitung_jumlah_data() > 0:
                kode = int(input("Masukkan kode yang akan dihapus: "))
                hapus_potion(kode)

        elif pilihan == "5":
            program_berjalan = False
            print("\n=== DATA AKHIR ===")
            tampilkan_semua_data()
            print("Terima kasih, program selesai.")

        else:
            print("Error: Pilih angka 1-5!")
            jumlah_error += 1

    except Exception as e:
        print(f"Terjadi error: {e}")
        jumlah_error += 1

print(f"\nTotal error selama program: {jumlah_error}")