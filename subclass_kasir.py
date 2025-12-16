from superclass import User
from connection import get_connection

class Kasir(User):
    def __init__(self, id=None, nama=None, umur=None, id_level=2,
                 username=None, password=None):
        super().__init__(id, nama, umur, id_level)
        self.__username = username
        self.__password = password

    # =========================
    # CREATE / INSERT
    # =========================
    def insert(self):
        super().insert()

        sql = """
            INSERT INTO kasir (id_kasir, username, password)
            VALUES (%s, %s, %s)
        """
        self.cursor.execute(
            sql,
            (self.get_id(), self.__username, self.__password)
        )
        self.conn.commit()
        print("Kasir berhasil ditambahkan....")

    # =========================
    # READ
    # =========================
    @staticmethod
    def select_by_id(id_kasir):
        conn = get_connection()
        cursor = conn.cursor()
        sql = """
            SELECT
                k.id_kasir,
                u.nama,
                k.username,
                k.password,
                u.umur
            FROM kasir k
            JOIN user u ON k.id_kasir = u.id
            WHERE k.id_kasir = %s
        """
        cursor.execute(sql, (id_kasir,))
        data = cursor.fetchone()
        cursor.close()
        conn.close()
        return data

    @staticmethod
    def get_all_kasir():
        conn = get_connection()
        cursor = conn.cursor()
        sql = """
            SELECT
                k.id_kasir,
                u.nama,
                u.umur,
                k.username,
                k.password
            FROM kasir k
            JOIN user u ON k.id_kasir = u.id
            WHERE u.id_level = 2
        """
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data

    # =========================
    # UPDATE
    # =========================
    def update(self):
        super().update()

        sql = """
            UPDATE kasir
            SET username=%s, password=%s
            WHERE id_kasir=%s
        """
        self.cursor.execute(
            sql,
            (self.__username, self.__password, self.get_id())
        )
        self.conn.commit()
        print("Kasir berhasil diupdate....")

    # =========================
    # DELETE
    # =========================
    def delete(self):
        sql = "DELETE FROM kasir WHERE id_kasir=%s"
        self.cursor.execute(sql, (self.get_id(),))
        self.conn.commit()

        User.delete(self.get_id())
        print("Kasir berhasil dihapus....")

    # =========================
    # LOGIN
    # =========================
    @staticmethod
    def cek_login(username, password):
        conn = get_connection()
        cursor = conn.cursor()
        sql = """
            SELECT k.id_kasir, u.nama
            FROM kasir k
            JOIN user u ON k.id_kasir = u.id
            WHERE k.username=%s
              AND k.password=%s
              AND u.id_level = 2
        """
        cursor.execute(sql, (username, password))
        data = cursor.fetchone()
        cursor.close()
        conn.close()
        return data

    @staticmethod
    def get_kasir_by_id(id_kasir):
        conn = get_connection()
        cursor = conn.cursor()
        sql = """
            SELECT
                k.id_kasir,
                u.nama,
                u.umur,
                k.username,
                k.password
            FROM kasir k
            JOIN user u ON k.id_kasir = u.id
            WHERE k.id_kasir = %s AND u.id_level = 2
        """
        cursor.execute(sql, (id_kasir,))
        data = cursor.fetchone()
        cursor.close()
        conn.close()
        return data
