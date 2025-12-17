# pemeriksaan.py
from connection import get_connection

class Pemeriksaan:
    def __init__(self, id=None, id_dokter=None, id_perawat=None, id_pasien=None, tanggal=None):
        self.id = id
        self.id_dokter = id_dokter
        self.id_perawat = id_perawat
        self.id_pasien = id_pasien
        self.tanggal = tanggal

    def insert(self):
        db = get_connection()
        cursor = db.cursor()

        sql = """
            INSERT INTO pemeriksaan 
            (id_dokter, id_perawat, id_pasien, tgl_pemeriksaan)
            VALUES (%s, %s, %s, %s)
        """
        val = (self.id_dokter, self.id_perawat, self.id_pasien, self.tanggal)

        cursor.execute(sql, val)
        db.commit()

        self.id = cursor.lastrowid

        cursor.close()
        db.close()

    @staticmethod
    def select_by_id(id_pem):
        db = get_connection()
        cursor = db.cursor()

        sql = """
            SELECT id_pemeriksaan, id_dokter, id_perawat, id_pasien, tgl_pemeriksaan
            FROM pemeriksaan
            WHERE id_pemeriksaan = %s
        """
        cursor.execute(sql, (id_pem,))
        data = cursor.fetchone()

        cursor.close()
        db.close()
        return data

    def update(self):
        db = get_connection()
        cursor = db.cursor()

        sql = """
            UPDATE pemeriksaan
            SET id_dokter=%s,
                id_perawat=%s,
                id_pasien=%s,
                tgl_pemeriksaan=%s
            WHERE id_pemeriksaan=%s
        """
        val = (
            self.id_dokter,
            self.id_perawat,
            self.id_pasien,
            self.tanggal,
            self.id
        )

        cursor.execute(sql, val)
        db.commit()

        cursor.close()
        db.close()

    def delete(self):
        db = get_connection()
        cursor = db.cursor()

        sql = "DELETE FROM pemeriksaan WHERE id_pemeriksaan=%s"
        cursor.execute(sql, (self.id,))
        db.commit()

        cursor.close()
        db.close()

    @staticmethod
    def select_detail_by_id(id_pem):
        db = get_connection()
        cursor = db.cursor()

        sql = """
            SELECT
                p.id_pemeriksaan,
                p.id_dokter,
                d.nama_dokter,
                p.id_perawat,
                pr.nama_perawat,
                p.id_pasien,
                ps.nama_pasien,
                p.tgl_pemeriksaan
            FROM pemeriksaan p
            JOIN dokter d ON p.id_dokter = d.id_dokter
            JOIN perawat pr ON p.id_perawat = pr.id_perawat
            JOIN pasien ps ON p.id_pasien = ps.id_pasien
            WHERE p.id_pemeriksaan = %s
        """
        cursor.execute(sql, (id_pem,))
        data = cursor.fetchone()

        cursor.close()
        db.close()
        return data
    
    def update_tanggal(self):
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            UPDATE pemeriksaan
            SET tgl_pemeriksaan = %s
            WHERE id_pemeriksaan = %s
        """
        cursor.execute(query, (self.tanggal, self.id))
        conn.commit()
        conn.close()
        
    def cari_data(self, id_pemeriksaan):
        db = get_connection()
        cursor = db.cursor()

        sql = """
            SELECT
                p.id_pemeriksaan,
                d.nama_dokter,
                pr.nama_perawat,
                ps.nama_pasien,
                ps.penyakit,
                p.tgl_pemeriksaan
            FROM pemeriksaan p
            JOIN dokter d ON p.id_dokter = d.id_dokter
            JOIN perawat pr ON p.id_perawat = pr.id_perawat
            JOIN pasien ps ON p.id_pasien = ps.id_pasien
            WHERE p.id_pemeriksaan = %s
        """
        cursor.execute(sql, (id_pemeriksaan,))
        data = cursor.fetchone()
        cursor.close()
        return data

    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor()
        sql = """
            SELECT
                id_pemeriksaan,
                id_dokter,
                id_perawat,
                id_pasien,
                tgl_pemeriksaan
            FROM pemeriksaan
        """
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data


    @staticmethod
    def get_by_id(id_pemeriksaan):
        conn = get_connection()
        cursor = conn.cursor()
        sql = """
            SELECT
                id_pemeriksaan,
                id_dokter,
                id_perawat,
                id_pasien,
                tgl_pemeriksaan
            FROM pemeriksaan
            WHERE id_pemeriksaan = %s
        """
        cursor.execute(sql, (id_pemeriksaan,))
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data
