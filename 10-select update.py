import sqlite3
koneksi = sqlite3.connect('fauna1.db')
kursor = koneksi.cursor()

id_fauna = 10
jml_skrng = 650

# mgunakan QUERY UPDATE
sql = (f"UPDATE fauna SET jml_skrng  = ? WHERE id_fauna = ?")
data = (jml_skrng, id_fauna)
kursor.execute(sql,data)
koneksi.commit()

#cek apakah data berhasil diubah atau belum
if kursor.rowcount > 0: #cek berdasarkan adanya baris atau tidak
    print(f"Data dengan ID {id_fauna} Berhasil diubah!!")
else:
    print(f"Tidak ada data fauna dengan ID {id_fauna}!")

kursor.execute("SELECT *FROM fauna")

baris_tabel = kursor.fetchall()

print("Data Fauna")
print("="*120)
print("{:<5} {:<20} {:<20} {:<15} {:<20}{:<20}".format("ID Fauna","Nama Fauna",
"Jenis","Asal", "Jml Sekarang", "Thn Terakir Ditemukan"))
print("-"*120)

# tampilkan data sesuai format tabel dengan perulangan
for baris in baris_tabel:
    print("{:<5}{:<20}{:<20}{:<20}{:<20}{:<20}".format(baris[0],baris[1],baris[2],baris[3],baris[4],baris[5]))

# putuskan koneksi  
koneksi.close