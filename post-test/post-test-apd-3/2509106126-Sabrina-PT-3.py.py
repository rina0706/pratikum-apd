print("\n=== Program Penggajian Karyawan PT. BOM===\n")

nama = input("Masukkan nama karyawan: ")
jabatan = input("Masukkan jabatan karyawan (peracik petasan/pengantar petasan): ")
hari_kerja = int(input("Masukkan jumlah hari kerja dalam sebulan: "))
jam_kerja = int(input("Masukkan jam kerja per hari: "))
jumlah_lembur = int(input("Masukkan jumlah lembur (jam): "))

if jabatan == "peracik petasan" and hari_kerja >= 18 and jam_kerja >= 6 and jumlah_lembur >= 2:
    bayaran_perjam = 20000
    bayaran_perlembur = 10000
elif jabatan == "peracik petasan" and hari_kerja >= 24 and jam_kerja >= 8 and jumlah_lembur >= 4:
    bayaran_perjam = 25000
    bayaran_perlembur = 15000
elif jabatan == "peracik petasan":
    bayaran_perjam = 15000
    bayaran_perlembur = 10000
elif jabatan == "pengantar petasan" and hari_kerja >= 16 and jam_kerja >= 5 and jumlah_lembur >= 4:
    bayaran_perjam = 20000
    bayaran_perlembur = 15000
elif jabatan == "pengantar petasan" and hari_kerja >= 20 and jam_kerja >= 7 and jumlah_lembur >= 7:
    bayaran_perjam = 25000
    bayaran_perlembur = 20000
elif jabatan == "pengantar petasan":
    bayaran_perjam = 15000
    bayaran_perlembur = 12000
else:
    bayaran_perjam = 15000
    bayaran_perlembur = 10000

total_gaji = (bayaran_perjam * jam_kerja * hari_kerja) + (jumlah_lembur * bayaran_perlembur)

print("===== Rincian Gaji =====")
print("Nama Karyawan :", nama)
print("Jabatan       :", jabatan)
print("Total Gaji    : Rp", total_gaji)



