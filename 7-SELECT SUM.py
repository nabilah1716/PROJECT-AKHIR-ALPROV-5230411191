import sqlite3
# koneksi database
koneksi = sqlite3.connect('fauna1.db')
kursor = koneksi.cursor()
kursor.execute("SELECT SUM(Jml_skrng) FROM FAUNA") # AVG rata2 SUM total
populasi_fauna = kursor.fetchone()[0] # AMBIL DATA GAJI JADIKAN BARIS BARU DIMULAI DARI INDEKS 0

print(f"Total Populasi Seluruh Fauna:{populasi_fauna} ")

koneksi.close()