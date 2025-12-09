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
            """SELECT dokter.id_dokter, user.nama, user.umur, dokter.spesialis
               FROM dokter JOIN user ON dokter.id_dokter=user.id"""
        )
        for row in cursor.fetchall():
            print(row)
        cursor.close()
        db.close()

    def update(self, nama, umur, spesialis):
        # Update USER
        self.set_nama(nama)
        self.set_umur(umur)
        super().update()

        # Update DOKTER
        db = get_connection()
        cursor = db.cursor()
        sql = "UPDATE dokter SET spesialis=%s WHERE id_dokter=%s"
        cursor.execute(sql, (spesialis, self.get_id()))
        db.commit()
        cursor.close()
        db.close()
        print("Dokter berhasil diupdate!")

    def delete(self):
        super().delete(self.get_id())
