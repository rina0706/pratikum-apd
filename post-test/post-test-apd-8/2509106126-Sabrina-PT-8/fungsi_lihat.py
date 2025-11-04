from data import dataPotion_Minecraft
from utilitas import hitung_jumlah_data
from prettytable import PrettyTable

def tampilkan_semua_data():
    print("\n=== DAFTAR POTION MINECRAFT ===")
    if hitung_jumlah_data() == 0:
        print("Tidak ada data!")
    else:
        table = PrettyTable()
        table.field_names = ["Kode", "Nama Potion"]
        for kode, nama in dataPotion_Minecraft.items():
            table.add_row([kode, nama])
        print(table)