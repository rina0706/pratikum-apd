from data import dataPotion_Minecraft

def cari_kode_terbesar():
    kode_terbesar = 0
    for kode in dataPotion_Minecraft:
        if kode > kode_terbesar:
            kode_terbesar = kode
    return kode_terbesar

def hitung_jumlah_data():
    jumlah = 0
    for _ in dataPotion_Minecraft:
        jumlah += 1
    return jumlah

def buat_kode_baru():
    if hitung_jumlah_data() == 0:
        return 1
    else:
        return cari_kode_terbesar() + 1