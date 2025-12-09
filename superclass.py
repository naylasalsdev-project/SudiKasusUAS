# superclass.py
from connection import get_connection

class User:
    def __init__(self, id=None, nama=None, umur=None, id_level=None):
        self.__id = id
        self.__nama = nama
        self.__umur = umur
        self.__id_level = id_level
        
        self.conn = get_connection()
        self.cursor = self.conn.cursor()

    # Getter
    def get_id(self):
        return self.__id

    def get_nama(self):
        return self.__nama

    def get_umur(self):
        return self.__umur

    def get_id_level(self):
        return self.__id_level

    # Setter
    def set_nama(self, nama):
        self.__nama = nama

    def set_umur(self, umur):
        self.__umur = umur

    def set_id_level(self, id_level):
        self.__id_level = id_level

    # CRUD dasar untuk USER
    def insert(self):
        sql = """INSERT INTO user (id, nama, umur, id_level)
                 VALUES (%s, %s, %s, %s)"""
        val = (self.__id, self.__nama, self.__umur, self.__id_level)
        self.cursor.execute(sql, val)
        self.conn.commit()
        print("User berhasil ditambahkan ke tabel USER!")

    @staticmethod
    def display():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM user")
        hasil = cursor.fetchall()
        for row in hasil:
            print(row)

    def update(self):
        sql = "UPDATE user SET nama=%s, umur=%s, id_level=%s WHERE id=%s"
        val = (self.__nama, self.__umur, self.__id_level, self.__id)
        self.cursor.execute(sql, val)
        self.conn.commit()
        print("User berhasil diupdate!")

    @staticmethod
    def delete(id):
        conn = get_connection()
        cursor = conn.cursor()
        sql = "DELETE FROM user WHERE id=%s"
        cursor.execute(sql, (id,))
        conn.commit()
        print("User dihapus dari tabel USER.")

    def login_admin(self, username, password):
        sql = "SELECT id_admin, nama FROM admin WHERE username=%s AND password=%s"
        self.cursor.execute(sql, (username, password))
        return self.cursor.fetchone()

    def login_kasir(self, username, password):
        sql = "SELECT id_kasir, nama FROM kasir WHERE username=%s AND password=%s"
        self.cursor.execute(sql, (username, password))
        return self.cursor.fetchone()