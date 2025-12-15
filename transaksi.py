# transaksi.py
from connection import get_connection

class Transaksi:
    def __init__(self, id_transaksi=None, id_pemeriksaan=None, tanggal=None, total_bayar=None):
        self.id_transaksi = id_transaksi
        self.id_pemeriksaan = id_pemeriksaan
        self.tanggal = tanggal
        self.total_bayar = total_bayar

    # ================= INSERT =================
    def insert(self):
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            INSERT INTO transaksi (id_pemeriksaan, tanggal, total_bayar)
            VALUES (%s, %s, %s)
        """
        cursor.execute(query, (
            self.id_pemeriksaan,
            self.tanggal,
            self.total_bayar
        ))
        conn.commit()

        # ambil id_transaksi terakhir (penting buat detail_transaksi)
        self.id_transaksi = cursor.lastrowid

        conn.close()
        return self.id_transaksi

    # ================= DISPLAY =================
    @staticmethod
    def display():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT 
                t.id_transaksi,
                p.id_pemeriksaan,
                d.nama_dokter,
                pr.nama_perawat,
                ps.nama_pasien,
                t.tanggal,
                t.total_bayar
            FROM transaksi t
            JOIN pemeriksaan p ON t.id_pemeriksaan = p.id_pemeriksaan
            JOIN dokter d ON p.id_dokter = d.id_dokter
            JOIN perawat pr ON p.id_perawat = pr.id_perawat
            JOIN pasien ps ON p.id_pasien = ps.id_pasien
        """)
        data = cursor.fetchall()
        conn.close()
        return data

    # ================= DELETE =================
    def delete(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM transaksi WHERE id_transaksi = %s",
            (self.id_transaksi,)
        )
        conn.commit()
        conn.close()

    # ================= CEK SUDAH TRANSAKSI =================
    @staticmethod
    def cek_transaksi(id_pemeriksaan):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM transaksi WHERE id_pemeriksaan = %s",
            (id_pemeriksaan,)
        )
        data = cursor.fetchone()
        conn.close()
        return data
