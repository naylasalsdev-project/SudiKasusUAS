# subclass_admin.py
from connection import get_connection
from superclass import User

class Admin(User):
    def __init__(self, id, nama, umur, username, password, id_level=1):
        super().__init__(id, nama, umur, id_level)
        self.__username = username
        self.__password = password

    def insert(self):
        super().insert()
        db = get_connection()
        cursor = db.cursor()
        sql = "INSERT INTO admin (id_admin, username, password) VALUES (%s, %s, %s)"
        cursor.execute(sql, (self.get_id(), self.__username, self.__password))
        db.commit()
        print("Admin berhasil ditambahkan!")

    @staticmethod
    def display():
        db = get_connection()
        cursor = db.cursor()
        cursor.execute(
            """SELECT admin.id_admin, user.nama, user.umur, admin.username
               FROM admin JOIN user ON admin.id_admin=user.id"""
        )
        for row in cursor.fetchall():
            print(row)

    def update(self, nama, umur, username, password):
        # Update di USER
        self.set_nama(nama)
        self.set_umur(umur)
        super().update()

        # Update di ADMIN
        db = get_connection()
        cursor = db.cursor()
        sql = "UPDATE admin SET username=%s, password=%s WHERE id_admin=%s"
        cursor.execute(sql, (username, password, self.get_id()))
        db.commit()
        print("Admin berhasil diupdate!")

    def delete(self):
        super().delete(self.get_id())

