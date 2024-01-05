import sqlite3
# koneksi database
koneksi = sqlite3.connect('fauna1.db')
# select all data pgw

kursor = koneksi.cursor()
# mengambil semua data dlm tabel dan tampilkan
kursor.execute("SELECT * FROM FAUNA ORDER BY jml_skrng DESC") # ASC terkecil DESC terbesar 
# TAMPILKAN DLM BENTUK GARIS
baris_table = kursor.fetchall()

print("Data Fauna")
print("="*110)
print("{:<5}{:20}{:<20}{:<20}{:<20}".format("ID Fauna","Nama Fauna","Jenis","Asal", "Jmlh Sekarang", "Thn Terakir Ditemukan"))
print("-"*110)
# tampilkan data sesuai format tabel dg perulangan
for baris in baris_table:
     print("{:<5}{:20}{:<20}{:<20}{:<20}{:<20}".format(str(baris[0]), baris[1], baris[2], baris[3], baris[4], baris[5]))
     
koneksi.close() 