# subclass_kasir.py
from connection import get_connection
from superclass import User

class Kasir(User):
    def __init__(self, id, nama, umur, username, password, id_level=2):
        super().__init__(id, nama, umur, id_level)
        self.__username = username
        self.__password = password

    def insert(self):
        super().insert()
        db = get_connection()
        cursor = db.cursor()
        sql = "INSERT INTO kasir (id_kasir, username, password) VALUES (%s, %s, %s)"
        cursor.execute(sql, (self.get_id(), self.__username, self.__password))
        db.commit()
        cursor.close()
        db.close()
        print("Kasir berhasil ditambahkan!")

    @staticmethod
    def display():
        db = get_connection()
        cursor = db.cursor()
        cursor.execute(
            """SELECT kasir.id_kasir, user.nama, user.umur, kasir.username
               FROM kasir JOIN user ON kasir.id_kasir=user.id"""
        )
        for row in cursor.fetchall():
            print(row)
        cursor.close()
        db.close()

    def update(self, nama, umur, username, password):
        # Update USER
        self.set_nama(nama)
        self.set_umur(umur)
        super().update()

        # Update KASIR
        db = get_connection()
        cursor = db.cursor()
        sql = "UPDATE kasir SET username=%s, password=%s WHERE id_kasir=%s"
        cursor.execute(sql, (username, password, self.get_id()))
        db.commit()
        cursor.close()
        db.close()
        print("Kasir berhasil diupdate!")

    def delete(self):
        super().delete(self.get_id())

    @staticmethod
    def cek_login(username, password):
        from connection import get_connection
        db = get_connection()
        cursor = db.cursor()

        sql = """SELECT kasir.id_kasir, user.nama
                 FROM kasir
                 JOIN user ON kasir.id_kasir = user.id
                 WHERE kasir.username=%s AND kasir.password=%s"""
        
        cursor.execute(sql, (username, password))
        hasil = cursor.fetchone()

        cursor.close()
        db.close()
        return hasil
    
    @staticmethod
    def select_by_id(id_kasir):
        db = get_connection()
        cursor = db.cursor()
        sql = """SELECT kasir.id_kasir, user.nama, kasir.username, kasir.password, user.umur, user.id_level
                 FROM kasir
                 JOIN user ON kasir.id_kasir = user.id
                 WHERE kasir.id_kasir=%s"""
        cursor.execute(sql, (id_kasir,))
        data = cursor.fetchone()
        cursor.close()
        db.close()
        return data