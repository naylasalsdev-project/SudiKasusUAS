from superclass import User
from connection import get_connection


class Dokter(User):
    def __init__(self, id, nama, umur, id_level, spesialis):
        super().__init__(id, nama, umur, id_level)
        self._spesialis = spesialis

    def insert(self):
        # 1️⃣ insert ke user
        super().insert()

        # 2️⃣ insert ke dokter (ISI nama_dokter)
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            INSERT INTO dokter (id_dokter, nama_dokter, spesialis)
            VALUES (%s, %s, %s)
        """
        cursor.execute(
            query,
            (self.get_id(), self.get_nama(), self._spesialis)
        )
        conn.commit()
        conn.close()

    # ================= DISPLAY =================
    @staticmethod
    def display():
        db = get_connection()
        cursor = db.cursor()
        cursor.execute("""
            SELECT dokter.id_dokter, user.nama, user.umur, dokter.spesialis, level.nama_level
            FROM dokter
            JOIN user ON dokter.id_dokter = user.id
            JOIN level ON user.id_level = level.id_level
        """)
        data = cursor.fetchall()
        cursor.close()
        db.close()
        return data

    # ================= UPDATE =================
    def update(self):
        # update user
        super().update()

        # update dokter
        conn = get_connection()
        cursor = conn.cursor()
        query = """
            UPDATE dokter
            SET nama_dokter=%s, spesialis=%s
            WHERE id_dokter=%s
        """
        cursor.execute(
            query,
            (self.get_nama(), self._spesialis, self.get_id())
        )
        conn.commit()
        conn.close()

    # ================= DELETE =================
    @staticmethod
    def delete(id_dokter):
        # 1️⃣ hapus dari tabel dokter dulu
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM dokter WHERE id_dokter=%s",
            (id_dokter,)
        )
        conn.commit()
        conn.close()

        # 2️⃣ hapus dari user
        User.delete(id_dokter)
        

    # ================= SELECT BY ID =================
    @staticmethod
    def select_by_id(id_dokter):
        db = get_connection()
        cursor = db.cursor()
        cursor.execute("""
            SELECT dokter.id_dokter, user.nama, user.umur, dokter.spesialis, level.nama_level, user.id_level
            FROM dokter
            JOIN user ON dokter.id_dokter = user.id
            JOIN level ON user.id_level = level.id_level
            WHERE dokter.id_dokter = %s
        """, (id_dokter,))
        data = cursor.fetchone()
        cursor.close()
        db.close()
        return data

    # ================= UNTUK TABEL =================
    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT
                d.id_dokter,
                u.nama,
                u.umur,
                d.spesialis
            FROM dokter d
            JOIN user u ON d.id_dokter = u.id
        """)
        data = cursor.fetchall()
        conn.close()
        return data

    @staticmethod
    def get_by_id(id_dokter):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT
                d.id_dokter,
                u.nama,
                u.umur,
                d.spesialis
            FROM dokter d
            JOIN user u ON d.id_dokter = u.id
            WHERE d.id_dokter = %s
        """, (id_dokter,))
        data = cursor.fetchall()
        conn.close()
        return data
    
    @staticmethod
    def get_spesialis_id(id_dokter):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT d.spesialis
            FROM dokter d
            WHERE d.id_dokter = %s
        """, (id_dokter,))
        data = cursor.fetchall()
        conn.close()
        return data    