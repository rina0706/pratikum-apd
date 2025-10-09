# Input berdasarkan NIM 2409106129 (digit terakhir kedua = 2)
jumlah_koridor = 2
data_intelijen = 0
perangkap_dijinakkan = 0

print("\n=== MISI KETIGA - PENYELIDIKAN ===")
print(f"Jumlah koridor: {jumlah_koridor}")

# Nested loop untuk koridor dan ruangan
for koridor in range(1, jumlah_koridor + 1):
    print(f"\nMemasuki Koridor {koridor}:")
    
    for ruangan in range(1, 4):  # Setiap koridor memiliki 3 ruangan
        nomor_ruangan = (koridor - 1) * 3 + ruangan
        
        if nomor_ruangan % 2 == 1:  # Ganjil = Data Intelijen
            data_intelijen += 1
            print(f"  Ruangan {ruangan} (No.{nomor_ruangan}) - 📊 Data Intelijen ditemukan!")
        else:  # Genap = Perangkap Peledak
            perangkap_dijinakkan += 1
            print(f"  Ruangan {ruangan} (No.{nomor_ruangan}) - 💣 Perangkap Peledak berhasil dijinakkan!")

print("\n=== HASIL MISI KETIGA ===")
print(f"Total Data Intelijen yang didapat: {data_intelijen}")
print(f"Total Perangkap Peledak yang dijinakkan: {perangkap_dijinakkan}")