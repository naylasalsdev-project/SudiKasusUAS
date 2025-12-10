from superclass import User
from connection import get_connection

class Admin(User):
    def __init__(self, id=None, nama=None, username=None, password=None, umur=None, id_level=1):
        super().__init__(id, nama, umur, id_level)
        self.__username = username
        self.__password = password


    def insert(self, id_admin, nama, username, password, umur, level):
     
        self._User__id = id_admin
        self._User__nama = nama
        self._User__umur = umur
        self._User__id_level = level
        
        self.__username = username
        self.__password = password


        super().insert()


        db = get_connection()
        cursor = db.cursor()

        sql = """
            INSERT INTO admin (id_admin, username, password)
            VALUES (%s, %s, %s)
        """

        cursor.execute(sql, (id_admin, username, password))
        db.commit()
        cursor.close()
        db.close()

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
        cursor.close()
        db.close()

    def update(self, id_admin, nama, username, password, umur, level):
    
        self._User__id = id_admin
        self._User__nama = nama
        self._User__umur = umur
        self._User__id_level = level

        self.__username = username
        self.__password = password
        
        super().update()

    
        db = get_connection()
        cursor = db.cursor()
        sql = "UPDATE admin SET username=%s, password=%s WHERE id_admin=%s"
        cursor.execute(sql, (username, password, id_admin))
        db.commit()
        cursor.close()
        db.close()

        print("Admin berhasil diupdate!")


    def delete(self, id_admin):
        db = get_connection()
        cursor = db.cursor()
        
        super().delete(id_admin)

        sql_admin = "DELETE FROM admin WHERE id_admin=%s"
        cursor.execute(sql_admin, (id_admin,))


        db.commit()
        cursor.close()
        db.close()

        print("Admin berhasil dihapus!")
        
    @staticmethod
    def cek_login(username, password):
        from connection import get_connection
        db = get_connection()
        cursor = db.cursor()

        sql = """SELECT admin.id_admin, user.nama
                 FROM admin
                 JOIN user ON admin.id_admin = user.id
                 WHERE admin.username=%s AND admin.password=%s"""
        
        cursor.execute(sql, (username, password))
        hasil = cursor.fetchone()

        cursor.close()
        db.close()
        return hasil
    
    @staticmethod
    def select_by_id(id_admin):
        db = get_connection()
        cursor = db.cursor()
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
        db.close()
        return data
    

