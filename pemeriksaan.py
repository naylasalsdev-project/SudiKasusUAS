# pemeriksaan.py
from connection import get_connection

class Pemeriksaan:
    def __init__(self, id_pem=None, id_dokter=None, id_perawat=None, id_pasien=None, tanggal=None):
        self.id_pem = id_pem
        self.id_dokter = id_dokter
        self.id_perawat = id_perawat
        self.id_pasien = id_pasien
        self.tanggal = tanggal

    def insert(self):
        db = get_connection()
        cursor = db.cursor()
        # id_pemeriksaan auto increment -> jangan isi manual
        sql = "INSERT INTO pemeriksaan (id_dokter, id_perawat, id_pasien, tgl_pemeriksaan) VALUES (%s, %s, %s, %s)"
        val = (self.id_dokter, self.id_perawat, self.id_pasien, self.tanggal)
        cursor.execute(sql, val)
        db.commit()
        # simpan id auto increment ke self.id_pem kalau mau
        try:
            self.id_pem = cursor.lastrowid
        except Exception:
            pass
        cursor.close()
        db.close()
        print("Data pemeriksaan berhasil ditambahkan!")

    @staticmethod
    def display():
        db = get_connection()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM pemeriksaan")
        for row in cursor.fetchall():
            print(row)
        cursor.close()
        db.close()

    def update(self, dokter_baru, perawat_baru, pasien_baru, tanggal_baru):
        db = get_connection()
        cursor = db.cursor()
        sql = "UPDATE pemeriksaan SET id_dokter=%s, id_perawat=%s, id_pasien=%s, tgl_pemeriksaan=%s WHERE id_pemeriksaan=%s"
        val = (dokter_baru, perawat_baru, pasien_baru, tanggal_baru, self.id_pem)
        cursor.execute(sql, val)
        db.commit()
        cursor.close()
        db.close()
        print("Data pemeriksaan berhasil diupdate!")

    def delete(self):
        db = get_connection()
        cursor = db.cursor()
        sql = "DELETE FROM pemeriksaan WHERE id_pemeriksaan=%s"
        cursor.execute(sql, (self.id_pem,))
        db.commit()
        cursor.close()
        db.close()
        print("Data pemeriksaan berhasil dihapus!")
