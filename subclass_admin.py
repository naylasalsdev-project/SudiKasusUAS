# subclass_admin.py
from superclass import User
from connection import get_connection

class Admin(User):
    def __init__(self, id=None, nama=None, umur=None, id_level=1,
                 username=None, password=None):
        super().__init__(id, nama, umur, id_level)
        self.__username = username
        self.__password = password

    # =========================
    # CREATE / INSERT
    # =========================
    def insert(self):
        # insert ke tabel USER
        super().insert()

        # insert ke tabel ADMIN
        sql = """
            INSERT INTO admin (id_admin, username, password)
            VALUES (%s, %s, %s)
        """
        self.cursor.execute(sql, (self.get_id(), self.__username, self.__password))
        self.conn.commit()
        print("Admin berhasil ditambahkan....")

    # =========================
    # READ
    # =========================
    @staticmethod
    def display():
        conn = get_connection()
        cursor = conn.cursor()
        sql = """
            SELECT admin.id_admin,
                   user.nama,
                   user.umur,
                   admin.username
            FROM admin
            JOIN user ON admin.id_admin = user.id
        """
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data

    @staticmethod
    def select_by_id(id_admin):
        conn = get_connection()
        cursor = conn.cursor()
        sql = """
            SELECT admin.id_admin,
                   user.nama,
                   admin.username,
                   admin.password,
                   user.umur,
                   level.nama_level
            FROM admin
            JOIN user ON admin.id_admin = user.id
            JOIN level ON user.id_level = level.id_level
            WHERE admin.id_admin=%s
        """
        cursor.execute(sql, (id_admin,))
        data = cursor.fetchone()
        cursor.close()
        conn.close()
        return data

    # =========================
    # UPDATE
    # =========================
    def update(self):
        # update tabel USER
        super().update()

        # update tabel ADMIN
        sql = """
            UPDATE admin
            SET username=%s, password=%s
            WHERE id_admin=%s
        """
        self.cursor.execute(sql, (self.__username, self.__password, self.get_id()))
        self.conn.commit()
        print("Admin berhasil diupdate....")

    # =========================
    # DELETE
    # =========================
    def delete(self):
        # hapus dari admin dulu
        sql = "DELETE FROM admin WHERE id_admin=%s"
        self.cursor.execute(sql, (self.get_id(),))
        self.conn.commit()

        # hapus dari user
        User.delete(self.get_id())
        print("Admin berhasil dihapus....")

    # =========================
    # LOGIN
    # =========================
    @staticmethod
    def cek_login(username, password):
        conn = get_connection()
        cursor = conn.cursor()
        sql = """
            SELECT admin.id_admin, user.nama
            FROM admin
            JOIN user ON admin.id_admin = user.id
            WHERE admin.username=%s AND admin.password=%s
        """
        cursor.execute(sql, (username, password))
        data = cursor.fetchone()
        cursor.close()
        conn.close()
        return data
