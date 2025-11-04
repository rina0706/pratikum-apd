from data import dataPotion_Minecraft

def hapus_potion(kode):
    if kode in dataPotion_Minecraft:
        del dataPotion_Minecraft[kode]
        print("Data berhasil dihapus!")
    else:
        print("Error: Kode tidak ditemukan!")