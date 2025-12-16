from connection import get_connection
from superclass import User

class Pasien(User):
    def __init__(self, id, nama, umur, penyakit, id_level=7):
        super().__init__(id, nama, umur, id_level)
        self._penyakit = penyakit

    def insert(self):
        # 1️⃣ insert ke user (ADA nama)
        super().insert()

        # 2️⃣ insert ke pasien (ISI nama_pasien juga)
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            INSERT INTO pasien (id_pasien, nama_pasien, penyakit)
            VALUES (%s, %s, %s)
        """
        cursor.execute(query, (self.get_id(), self.get_nama(), self._penyakit))
        conn.commit()
        conn.close()

    @staticmethod
    def display():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT pasien.id_pasien, user.nama, user.umur, pasien.penyakit
            FROM pasien
            JOIN user ON pasien.id_pasien = user.id
        """)
        data = cursor.fetchall()
        conn.close()
        return data

    def update(self):
        # update user
        super().update()

        # update pasien
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            UPDATE pasien
            SET penyakit = %s
            WHERE id_pasien = %s
        """
        cursor.execute(query, (self._penyakit, self.get_id()))
        conn.commit()
        conn.close()

    def delete(self):
        # hapus pasien & user
        super().delete(self.get_id())

    @staticmethod
    def select_by_id(id_pasien):
        conn = get_connection()
        cursor = conn.cursor()
        query = """
                SELECT pasien.id_pasien,
                user.nama,
                user.umur,
                pasien.penyakit
            FROM pasien
            JOIN user ON pasien.id_pasien = user.id
            WHERE pasien.id_pasien = %s
        """
        cursor.execute(query, (id_pasien,))
        data = cursor.fetchone()
        conn.close()
        return data
    
    # =========================
    # READ (UNTUK GUI)
    # =========================
    @staticmethod
    def get_all_pasien():
        conn = get_connection()
        cursor = conn.cursor()
        sql = """
            SELECT
                p.id_pasien,
                u.nama,
                u.umur,
                p.penyakit
            FROM pasien p
            JOIN user u ON p.id_pasien = u.id
        """
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data


    @staticmethod
    def get_pasien_by_id(id_pasien):
        conn = get_connection()
        cursor = conn.cursor()
        sql = """
            SELECT
                p.id_pasien,
                u.nama,
                u.umur
            FROM pasien p
            JOIN user u ON p.id_pasien = u.id
            WHERE p.id_pasien = %s
        """
        cursor.execute(sql, (id_pasien,))
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data

