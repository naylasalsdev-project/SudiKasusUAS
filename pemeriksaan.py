from connection import get_connection

class Pemeriksaan:
    def __init__(self, id_pem, id_dokter, id_perawat, id_pasien, tanggal):
        self.id_pem = id_pem
        self.id_dokter = id_dokter
        self.id_perawat = id_perawat
        self.id_pasien = id_pasien
        self.tanggal = tanggal

    def insert(self):
        db = get_connection()
        cursor = db.cursor()
        sql = "INSERT INTO pemeriksaan (id_pemeriksaan, id_dokter, id_perawat, id_pasien, tgl_pemeriksaan) VALUES (%s, %s, %s, %s, %s)"
        val = (self.id_pem, self.id_dokter, self.id_perawat, self.id_pasien, self.tanggal)
        cursor.execute(sql, val)
        db.commit()
        print("Data pemeriksaan berhasil ditambahkan!")

    @staticmethod
    def display():
        db = get_connection()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM pemeriksaan")
        for row in cursor.fetchall():
            print(row)

    def update(self, dokter_baru, perawat_baru, pasien_baru, tanggal_baru):
        db = get_connection()
        cursor = db.cursor()
        sql = "UPDATE pemeriksaan SET id_dokter=%s, id_perawat=%s, id_pasien=%s, tgl_pemeriksaan=%s WHERE id_pemeriksaan=%s"
        val = (dokter_baru, perawat_baru, pasien_baru, tanggal_baru, self.id_pem)
        cursor.execute(sql, val)
        db.commit()
        print("Data pemeriksaan berhasil diupdate!")

    def delete(self):
        db = get_connection()
        cursor = db.cursor()
        sql = "DELETE FROM pemeriksaan WHERE id_pemeriksaan=%s"
        cursor.execute(sql, (self.id_pem,))
        db.commit()
        print("Data pemeriksaan berhasil dihapus!")
