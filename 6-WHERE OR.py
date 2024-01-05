import sqlite3
# koneksi database
koneksi = sqlite3.connect('fauna1.db')
# select all data pgw

kursor = koneksi.cursor()
# mengambil semua data dlm tabel dan tampilkan
kursor.execute("SELECT *FROM FAUNA WHERE Asal = 'Sumatera' OR Jml_skrng >=500 ")
# TAMPILKAN DLM BENTUK GARIS
baris_tabel = kursor.fetchall()

print("Data Pegawai Kwangya 2024")
print("="*80)
print("{:<5}{:20}{:<20}{:<20}{:<20}{:<20}".format("ID Fauna","Nama Fauna","Jenis","Asal", "Jmlh Sekarang", "Thn Terakir Ditemukan"))
print("-"*80)
# tampilkan data sesuai format tabel dg perulangan
for baris in baris_tabel:
     print("{:<5}{:20}{:<20}{:<20}{:<20}{:<20}".format(str(baris[0]), baris[1], baris[2], baris[3], baris[4], baris[5]))
     
koneksi.close() 