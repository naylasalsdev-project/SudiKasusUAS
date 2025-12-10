# subclass_dokter.py
from connection import get_connection
from superclass import User

class Dokter(User):
    def __init__(self, id, nama, umur, spesialis, id_level=None):
        # default id_level = 3 (dokter spesialis) jika tidak diberikan
        if id_level is None:
            id_level = 3
        super().__init__(id, nama, umur, id_level)
        self.__spesialis = spesialis

    def insert(self):
        super().insert()
        db = get_connection()
        cursor = db.cursor()
        sql = "INSERT INTO dokter (id_dokter, spesialis) VALUES (%s, %s)"
        cursor.execute(sql, (self.get_id(), self.__spesialis))
        db.commit()
        cursor.close()
        db.close()
        print("Dokter berhasil ditambahkan!")

    @staticmethod
    def display():
        db = get_connection()
        cursor = db.cursor()
        cursor.execute(
        """SELECT dokter.id_dokter, user.nama, user.umur, dokter.spesialis, level.nama_level
        FROM dokter
        JOIN user ON dokter.id_dokter = user.id
        JOIN level ON user.id_level = level.id_level"""
        )
        for row in cursor.fetchall():
            print(row)
        cursor.close()
        db.close()

    def update(self, nama, umur, spesialis, id_level):
        # Update nilai objek terlebih dahulu
        self.set_nama(nama)
        self.set_umur(umur)
        self.set_id_level(id_level)
        self.__spesialis = spesialis     # ← INI PENTING BANGET!

        # Update USER (nama, umur, level)
        super().update()

        # Update DOKTER (spesialis)
        db = get_connection()
        cursor = db.cursor()
        sql = "UPDATE dokter SET spesialis=%s WHERE id_dokter=%s"
        cursor.execute(sql, (self.__spesialis, self.get_id()))
        db.commit()
        cursor.close()
        db.close()

        print("Dokter berhasil diupdate!")

    def delete(self):
        super().delete(self.get_id())
     
    @staticmethod   
    def select_by_id(id_dokter):
        db = get_connection()
        cursor = db.cursor()
        sql = """SELECT dokter.id_dokter, user.nama, user.umur, level.nama_level
                 FROM dokter
                 JOIN user ON dokter.id_dokter = user.id
                 JOIN level ON user.id_level = level.id_level
                 WHERE dokter.id_dokter=%s"""
        cursor.execute(sql, (id_dokter,))
        data = cursor.fetchone()
        cursor.close()
        db.close()
        return data
