from data import dataPotion_Minecraft

def ubah_potion(kode, nama_baru):
    if kode in dataPotion_Minecraft:
        dataPotion_Minecraft[kode] = nama_baru
        print("Data berhasil diubah!")
    else:
        print("Error: Kode tidak ditemukan!")