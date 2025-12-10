from connection import get_connection
from superclass import User

class Dokter(User):
    def __init__(self, id, nama, umur, id_level=3):
        super().__init__(id, nama, umur, id_level)

    def insert(self):
        # insert ke tabel user (superclass)
        super().insert()

        # insert ke tabel dokter
        db = get_connection()
        cursor = db.cursor()
        sql = "INSERT INTO dokter (id_dokter) VALUES (%s)"
        cursor.execute(sql, (self.get_id(),))
        db.commit()

        cursor.close()
        db.close()

    @staticmethod
    def display():
        db = get_connection()
        cursor = db.cursor()
        cursor.execute("""
            SELECT dokter.id_dokter, user.nama, user.umur, level.nama_level
            FROM dokter
            JOIN user ON dokter.id_dokter = user.id
            JOIN level ON user.id_level = level.id_level
        """)
        data = cursor.fetchall()

        cursor.close()
        db.close()
        return data

    def update(self):
        # update tabel user
        super().update()

        print("Dokter berhasil diupdate!")


    @staticmethod
    def delete(id_dokter):
        db = get_connection()
        cursor = db.cursor()
        sql = "DELETE FROM dokter WHERE id_dokter=%s"
        val = (id_dokter,)
        cursor.execute(sql, val)
        cursor.close()
        db.commit()
        deleted = cursor.rowcount
        db.disconnect()
        return deleted

    @staticmethod
    def select_by_id(id_dokter):
        db = get_connection()
        cursor = db.cursor()
        cursor.execute("""
            SELECT dokter.id_dokter, user.nama, user.umur, level.nama_level, user.id_level
            FROM dokter
            JOIN user ON dokter.id_dokter = user.id
            JOIN level ON user.id_level = level.id_level
            WHERE dokter.id_dokter = %s
        """, (id_dokter,))
        data = cursor.fetchone()

        cursor.close()
        db.close()
        return data
