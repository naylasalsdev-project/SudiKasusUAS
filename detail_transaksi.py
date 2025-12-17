# detail_transaksi.py
from connection import get_connection

class DetailTransaksi:
    def __init__(self, id_transaksi=None, id_layanan=None):
        self.id_transaksi = id_transaksi
        self.id_layanan = id_layanan

    def insert(self):
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            INSERT INTO detail_transaksi (id_transaksi, id_layanan)
            VALUES (%s, %s)
        """
        cursor.execute(query, (
            self.id_transaksi,
            self.id_layanan
        ))
        conn.commit()
        conn.close()

    @staticmethod
    def get_by_transaksi(id_transaksi):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT 
                l.nama_layanan,
                l.biaya
            FROM detail_transaksi dt
            JOIN layanan l ON dt.id_layanan = l.id_layanan
            WHERE dt.id_transaksi = %s
        """, (id_transaksi,))
        data = cursor.fetchall()
        conn.close()
        return data
