# subclass_perawat.py
from connection import get_connection
from superclass import User

class Perawat(User):
    def __init__(self, id, nama, umur, shift, id_level):
        super().__init__(id, nama, umur, id_level)
        self.__shift = shift

    def insert(self):
        super().insert()
        db = get_connection()
        cursor = db.cursor()
        sql = "INSERT INTO perawat (id_perawat, shift) VALUES (%s, %s)"
        cursor.execute(sql, (self.get_id(), self.__shift))
        db.commit()
        print("Perawat berhasil ditambahkan!")

    @staticmethod
    def display():
        db = get_connection()
        cursor = db.cursor()
        cursor.execute(
            """SELECT perawat.id_perawat, user.nama, user.umur, perawat.shift
               FROM perawat JOIN user ON perawat.id_perawat=user.id"""
        )
        for row in cursor.fetchall():
            print(row)

    def update(self, nama, umur, shift):
        # Update USER
        self.set_nama(nama)
        self.set_umur(umur)
        super().update()

        # Update PERAWAT
        db = get_connection()
        cursor = db.cursor()
        sql = "UPDATE perawat SET shift=%s WHERE id_perawat=%s"
        cursor.execute(sql, (shift, self.get_id()))
        db.commit()
        print("Perawat berhasil diupdate!")

    def delete(self):
        super().delete(self.get_id())

