nama = input("Masukkan nama pelanggan: ")
jumlah_batubata = int(input("Masukkan jumlah batu bata yang dibeli: "))
jumlah_semen = int(input("Masukkan jumlah karung semen yang dibeli: "))

# Harga satuan
harga_batubata = 100
harga_semen = 100000

# Hitung total biaya awal (sebelum diskon)
total_awal = (jumlah_batubata * harga_batubata) + (jumlah_semen * harga_semen)

# Tentukan diskon berdasarkan kondisi
diskon = 0

if jumlah_batubata == 500 and jumlah_semen == 5:
    diskon = 0.15   # 15% diskon
elif jumlah_batubata == 2000 and jumlah_semen == 16:
    diskon = 0.30   # 30% diskon

# Hitung total setelah diskon
total_diskon = total_awal * diskon
total_bayar = total_awal - total_diskon

# Tampilkan hasil
print("\n===== STRUK PEMBELIAN =====")
print(f"Nama Pelanggan : {nama}")
print(f"Jumlah Batu Bata : {jumlah_batubata} x Rp{harga_batubata:,}")
print(f"Jumlah Karung Semen : {jumlah_semen} x Rp{harga_semen:,}")
print(f"Total Awal : Rp{total_awal:,}")
print(f"Diskon : {diskon*100}% (Rp{total_diskon:,})")
print(f"Total Bayar : Rp{total_bayar:,}")
print("============================")