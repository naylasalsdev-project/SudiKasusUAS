# subclass_pasien.py
from connection import get_connection
from superclass import User

class Pasien(User):
    def __init__(self, id, nama, umur, penyakit, id_level=None):
        if id_level is None:
            id_level = 7
        super().__init__(id, nama, umur, id_level)
        self.__penyakit = penyakit

    def insert(self):
        super().insert()
        db = get_connection()
        cursor = db.cursor()
        sql = "INSERT INTO pasien (id_pasien, penyakit) VALUES (%s, %s)"
        cursor.execute(sql, (self.get_id(), self.__penyakit))
        db.commit()
        cursor.close()
        db.close()
        print("Pasien berhasil ditambahkan!")

    @staticmethod
    def display():
        db = get_connection()
        cursor = db.cursor()
        cursor.execute(
            """SELECT pasien.id_pasien, user.nama, user.umur, pasien.penyakit
               FROM pasien JOIN user ON pasien.id_pasien=user.id"""
        )
        for row in cursor.fetchall():
            print(row)
        cursor.close()
        db.close()

    def update(self, nama, umur, penyakit):
        # Update USER
        self.set_nama(nama)
        self.set_umur(umur)
        super().update()

        # Update PASIEN
        db = get_connection()
        cursor = db.cursor()
        sql = "UPDATE pasien SET penyakit=%s WHERE id_pasien=%s"
        cursor.execute(sql, (penyakit, self.get_id()))
        db.commit()
        cursor.close()
        db.close()
        print("Pasien berhasil diupdate!")

    def delete(self):
        super().delete(self.get_id())
