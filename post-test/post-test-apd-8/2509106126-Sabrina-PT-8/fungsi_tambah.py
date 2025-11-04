from data import dataPotion_Minecraft
from utilitas import buat_kode_baru

def tambah_potion(nama_potion):
    kode_baru = buat_kode_baru()
    dataPotion_Minecraft[kode_baru] = nama_potion
    print(f"Berhasil tambah {nama_potion} dengan kode {kode_baru}")