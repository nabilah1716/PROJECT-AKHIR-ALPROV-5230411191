# query like
import sqlite3
# koneksi database
koneksi = sqlite3.connect('fauna1.db')
kursor = koneksi.cursor()
# menjalankan query select dgn like
# misalkan kita ingin mencari nama dengan awalan huruf D
nama = 'B%'
kursor.execute(f"SELECT * FROM FAUNA WHERE nama_fauna LIKE ?" , (nama,))
baris_table = kursor.fetchall()
# membuat format table dengan method format
print("Data Fauna")
print("="*80)
print("{:<5}{:20}{:<20}{:<20}{:<20}".format("ID Fauna","Nama Fauna","Jenis","Asal", "Jmlh Sekarang", "Thn Terakir Ditemukan"))
print("-"*80)
# tampilkan data sesuai format tabel dg perulangan
for baris in baris_table:
     print("{:<5}{:20}{:<20}{:<20}{:<20}{:<20}".format(str(baris[0]), baris[1], baris[2], baris[3], baris[4], baris[5]))
     
koneksi.close()