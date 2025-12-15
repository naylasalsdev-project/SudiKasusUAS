# layanan.py
from connection import get_connection

class Layanan:
    def __init__(self, id_layanan=None, nama_layanan=None, biaya=None):
        self.id_layanan = id_layanan
        self.nama_layanan = nama_layanan
        self.biaya = biaya

    # ================= INSERT =================
    def insert(self):
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            INSERT INTO layanan (nama_layanan, biaya)
            VALUES (%s, %s)
        """
        cursor.execute(query, (self.nama_layanan, self.biaya))
        conn.commit()
        conn.close()

    # ================= DISPLAY =================
    @staticmethod
    def display():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id_layanan, nama_layanan, biaya FROM layanan")
        data = cursor.fetchall()
        conn.close()
        return data
    
    def update(self):
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            UPDATE layanan
            SET nama_layanan=%s, biaya=%s
            WHERE id_layanan=%s
        """
        cursor.execute(query, (self.nama_layanan, self.biaya, self.id_layanan))
        conn.commit()
        conn.close()

    @staticmethod
    def delete(id_layanan):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM layanan WHERE id_layanan=%s", (id_layanan,))
        conn.commit()
        conn.close()

    # ================= SELECT BY ID =================
    @staticmethod
    def select_by_id(id_layanan):
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            SELECT id_layanan, nama_layanan, biaya
            FROM layanan
            WHERE id_layanan = %s
        """
        cursor.execute(query, (id_layanan,))
        data = cursor.fetchone()
        conn.close()
        return data
    
    @staticmethod
    def select_by_nama(nama_layanan):
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            SELECT id_layanan, nama_layanan, biaya
            FROM layanan
            WHERE nama_layanan = %s
        """
        cursor.execute(query, (nama_layanan,))
        data = cursor.fetchone()
        conn.close()
        return data

    @staticmethod
    def get_biaya_by_id(id_layanan):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT biaya FROM layanan WHERE id_layanan = %s",
            (id_layanan,)
        )
        data = cursor.fetchone()
        conn.close()
        return data[0] if data else 0

    @staticmethod
    def hitung_total(id_layanan_list):
        total = 0
        for id_layanan in id_layanan_list:
            total += Layanan.get_biaya_by_id(id_layanan)
        return total