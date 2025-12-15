# transaksi.py
from connection import get_connection

class Transaksi:
    def __init__(self, id_transaksi=None, id_pemeriksaan=None, id_layanan=None, tanggal=None, total_bayar=None):
        self.id_transaksi = id_transaksi
        self.id_pemeriksaan = id_pemeriksaan
        self.id_layanan = id_layanan
        self.tanggal = tanggal
        self.total_bayar = total_bayar

    # ================= INSERT =================
    def insert(self):
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            INSERT INTO transaksi
            (id_pemeriksaan, id_layanan, tanggal, total_bayar)
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(
            query,
            (self.id_pemeriksaan, self.id_layanan, self.tanggal, self.total_bayar)
        )
        conn.commit()
        conn.close()

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
                l.nama_layanan,
                t.tanggal,
                t.total_bayar
            FROM transaksi t
            JOIN pemeriksaan p ON t.id_pemeriksaan = p.id_pemeriksaan
            JOIN dokter d ON p.id_dokter = d.id_dokter
            JOIN perawat pr ON p.id_perawat = pr.id_perawat
            JOIN pasien ps ON p.id_pasien = ps.id_pasien
            JOIN layanan l ON t.id_layanan = l.id_layanan
        """)
        data = cursor.fetchall()
        conn.close()
        return data
    
    def delete(self):
        conn = get_connection()
        cursor = conn.cursor()
        query = "DELETE FROM transaksi WHERE id_transaksi = %s"
        cursor.execute(query, (self.id_transaksi,))
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
