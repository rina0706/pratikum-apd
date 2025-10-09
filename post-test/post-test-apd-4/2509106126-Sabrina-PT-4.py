print("=== MISI PERTAMA - MENYEMPURNAKAN RASENGAN ===")
stamina = 126
chakra = 0

print(f'Stamina awal naruto: {stamina}')
print(f'Chakra awal naruto: {chakra}')

while chakra < 200 and stamina > 0:
    chakra += 5
    stamina -= 3

print("=== HASIL DARI MISI PERTAMA ===")
print("Chakra terkumpul:", chakra)
print("Sisa stamina:", stamina)

if chakra >= 200:
    print("Naruto berhasil mencapai 200 chakra!")
else:
    print("Naruto kehabisan stamina sebelum mencapai 200 chakra")


print("\n=== MISI KEDUA - INFILTRASI ===")
tinggi_menara = 26  
gulungan = 0
print(f'tinngi menara: {tinggi_menara}')

for meter in range(3, tinggi_menara + 1, 3):
    gulungan += 1

print("=== HASIL DARI MISI 2  ===")
print("Tinggi menara:", tinggi_menara, "meter")
print("Gulungan informasi yang didapatkan:", gulungan)

print("\n=== MISI KETIGA - PENYELIDIKAN ===")
jumlah_koridor = 2
data_intelejen = 0
perangkap_dijinakkan = 0

print(f'jumlah koridor: {jumlah_koridor}')
for koridor in range(1, jumlah_koridor + 1):
    print(f"Koridor {koridor}:")

    for ruangan in range(1, 4):
        nomor_ruangan = (koridor - 1) * 3 + ruangan

        if nomor_ruangan % 2 == 1:
            data_intelejen += 1
            print(f"  Ruangan {ruangan}: Data Intelijen ditemukan")
        else:
            print(f"  Ruangan {ruangan}: Perangkap Peledak dijinakkan")
            perangkap_dijinakkan += 1

print("=== HASIL DARI MISI 3 ===")
print("Total Data Intelijen:", data_intelejen)
print("Total Perangkap Peledak:", perangkap_dijinakkan)  