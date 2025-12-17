from superclass import User
from connection import get_connection


class Perawat(User):
    def __init__(self, id, nama, umur, shift, id_level=6):
        super().__init__(id, nama, umur, id_level)
        self._shift = shift

    def insert(self):
        super().insert()

        conn = get_connection()
        cursor = conn.cursor()
        query = """
            INSERT INTO perawat (id_perawat, nama_perawat, shift)
            VALUES (%s, %s, %s)
        """
        cursor.execute(
            query,
            (self.get_id(), self.get_nama(), self._shift)
        )
        conn.commit()
        conn.close()

    @staticmethod
    def display():
        db = get_connection()
        cursor = db.cursor()
        cursor.execute("""
            SELECT perawat.id_perawat, user.nama, user.umur, perawat.shift, level.nama_level
            FROM perawat
            JOIN user ON perawat.id_perawat = user.id
            JOIN level ON user.id_level = level.id_level
        """)
        data = cursor.fetchall()
        cursor.close()
        db.close()
        return data

    def update(self):
        super().update()

        db = get_connection()
        cursor = db.cursor()
        sql = """
            UPDATE perawat
            SET shift = %s
            WHERE id_perawat = %s
        """
        cursor.execute(sql, (self._shift, self.get_id()))
        db.commit()
        cursor.close()
        db.close()

    @staticmethod
    def delete(id_perawat):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM perawat WHERE id_perawat=%s",
            (id_perawat,)
        )
        conn.commit()
        conn.close()

        User.delete(id_perawat)

    @staticmethod
    def select_by_id(id_perawat):
        db = get_connection()
        cursor = db.cursor()
        cursor.execute("""
            SELECT perawat.id_perawat, user.nama, user.umur, perawat.shift, level.nama_level, user.id_level
            FROM perawat
            JOIN user ON perawat.id_perawat = user.id
            JOIN level ON user.id_level = level.id_level
            WHERE perawat.id_perawat = %s
        """, (id_perawat,))
        data = cursor.fetchone()
        cursor.close()
        db.close()
        return data

    @staticmethod
    def get_all():
        conn = get_connection()
        cursor = conn.cursor()
        sql = """
            SELECT
                p.id_perawat,
                u.nama,
                u.umur,
                p.shift
            FROM perawat p
            JOIN user u ON p.id_perawat = u.id
        """
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data

    @staticmethod
    def get_by_id(id_perawat):
        conn = get_connection()
        cursor = conn.cursor()
        sql = """
            SELECT
                p.id_perawat,
                u.nama,
                u.umur,
                p.shift
            FROM perawat p
            JOIN user u ON p.id_perawat = u.id
            WHERE p.id_perawat = %s
        """
        cursor.execute(sql, (id_perawat,))
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data
