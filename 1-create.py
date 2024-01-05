import sqlite3

# buat connection db
conn = sqlite3.connect('fauna1.db')

conn.execute('''
             CREATE TABLE fauna(
                 id_fauna INTEGER PRIMARY KEY AUTOINCREMENT,
                 nama_fauna VARCHAR(50),
                 jenis VARCHAR(50),
                 asal VARCHAR(50),
                 jml_skrng INTEGER(50),
                 thn_ditemukan INTEGER(50)
             )
             ''')

conn.close